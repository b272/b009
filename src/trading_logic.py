import pandas as pd
import time
import requests
import numpy as np
import logging
from datetime import datetime
from bybit_bot import BybitBot
from utils.config import Config
from analysis.price_prediction import enhance_trading_logic


logger = logging.getLogger(__name__)

class TradingLogic:
    def __init__(self, api_key, api_secret, symbol="BTCUSDT", interval="15", rsi_period=14, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.symbol = symbol
        self.interval = interval
        self.rsi_period = rsi_period
        self.base_url = "https://api-demo.bybit.com" if testnet else "https://api.bybit.com"
        self.position = None
        self.bot = BybitBot(api_key, api_secret, testnet)
        logger.info(f"Initialized TradingLogic for {symbol} with {interval}m interval")

    def get_klines(self):
        """Get candlestick data"""
        endpoint = "/v5/market/kline"
        params = f"category=linear&symbol={self.symbol}&interval={self.interval}&limit=100"
        timestamp = str(int(time.time() * 1000))
        signature = self.bot.generate_signature(params, timestamp)
        
        headers = {
            "X-BAPI-API-KEY": self.api_key,
            "X-BAPI-SIGN": signature,
            "X-BAPI-TIMESTAMP": timestamp,
            "X-BAPI-RECV-WINDOW": "5000"
        }
        
        response = requests.get(
            self.base_url + endpoint + "?" + params,
            headers=headers
        )
        return response.json()

    def calculate_indicators(self, df):
        """Calculate technical indicators"""
        # RSI
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=self.rsi_period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=self.rsi_period).mean()
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))
        
        # Moving Averages
        df['sma_20'] = df['close'].rolling(window=20).mean()
        df['sma_50'] = df['close'].rolling(window=50).mean()
        
        # Bollinger Bands
        df['bb_middle'] = df['close'].rolling(window=20).mean()
        df['bb_upper'] = df['bb_middle'] + 2 * df['close'].rolling(window=20).std()
        df['bb_lower'] = df['bb_middle'] - 2 * df['close'].rolling(window=20).std()
        
        # MACD
        exp1 = df['close'].ewm(span=12, adjust=False).mean()
        exp2 = df['close'].ewm(span=26, adjust=False).mean()
        df['macd'] = exp1 - exp2
        df['signal'] = df['macd'].ewm(span=9, adjust=False).mean()
        
        return df

    def analyze_market(self):
        """Perform market analysis"""
        klines = self.get_klines()
        df = pd.DataFrame(klines['result']['list'])
        df['close'] = pd.to_numeric(df[4])
        
        df = self.calculate_indicators(df)
        latest_data = df.iloc[-1]
        
        return {
            'rsi': latest_data['rsi'],
            'sma_20': latest_data['sma_20'],
            'sma_50': latest_data['sma_50'],
            'macd': latest_data['macd'],
            'signal': latest_data['signal'],
            'bb_upper': latest_data['bb_upper'],
            'bb_lower': latest_data['bb_lower']
        }

    def check_entry_conditions(self, analysis):
        """Check conditions for entering a trade"""
        # Verify we have analysis data
        if not analysis:
            logger.info("No analysis data available")
            return {'long': False, 'short': False}
        
        # Extract key metrics
        rsi = analysis.get('rsi', 0)
        sma_20 = analysis.get('sma_20', 0) 
        sma_50 = analysis.get('sma_50', 0)
        macd = analysis.get('macd', 0)
        signal = analysis.get('signal', 0)
        
        # Define entry conditions
        long_conditions = [
            sma_20 > sma_50,  # Uptrend
            rsi < Config.RSI_OVERSOLD,  # Oversold
            macd > signal  # Bullish MACD
        ]
        
        short_conditions = [
            sma_20 < sma_50,  # Downtrend
            rsi > Config.RSI_OVERBOUGHT,  # Overbought
            macd < signal  # Bearish MACD
        ]
        
        return {
            'long': all(long_conditions),
            'short': all(short_conditions)
        }





    def get_position(self):
        """Get current position information"""
        endpoint = "/v5/position/list"
        params = f"category=linear&symbol={self.symbol}"
        timestamp = str(int(time.time() * 1000))
        signature = self.bot.generate_signature(params, timestamp)
        
        headers = {
            "X-BAPI-API-KEY": self.api_key,
            "X-BAPI-SIGN": signature,
            "X-BAPI-TIMESTAMP": timestamp,
            "X-BAPI-RECV-WINDOW": "5000"
        }
        
        response = requests.get(
            self.base_url + endpoint + "?" + params,
            headers=headers
        )
        return response.json()    

    def execute_strategy(self):
        """Execute trading strategy"""
        try:
            # Get current market analysis
            analysis = self.analyze_market()
            logger.info("\n=== STRATEGY EXECUTION ===")
            logger.info(f"Time: {datetime.now()}")
            logger.info(f"Market Analysis: {analysis}")
            
            # Check entry conditions
            entry_signals = self.check_entry_conditions(analysis)
            logger.info(f"Entry Signals - Long: {entry_signals['long']}, Short: {entry_signals['short']}")
            
            # Get position info
            position_data = self.get_position()
            has_position = len(position_data.get('result', {}).get('list', [])) > 0
            
            if not has_position:
                if entry_signals['long']:
                    order = self.bot.place_order(
                        symbol=self.symbol,
                        side="Buy",
                        order_type="Market", 
                        qty=Config.QUANTITY
                    )
                    logger.info("\n[ORDER PLACED - LONG]")
                    logger.info(f"Symbol: {self.symbol}")
                    logger.info(f"Quantity: {Config.QUANTITY}")
                    logger.info(f"Order Details: {order}")
                    
                elif entry_signals['short']:
                    order = self.bot.place_order(
                        symbol=self.symbol,
                        side="Sell",
                        order_type="Market",
                        qty=Config.QUANTITY
                    )
                    logger.info("\n[ORDER PLACED - SHORT]")
                    logger.info(f"Symbol: {self.symbol}")
                    logger.info(f"Quantity: {Config.QUANTITY}")
                    logger.info(f"Order Details: {order}")
            
            else:
                current_position = position_data['result']['list'][0]
                position_size = abs(float(current_position['size']))
                position_side = current_position['side']
                
                if position_side == "Buy" and (analysis['rsi'] > 70 or analysis['sma_20'] < analysis['sma_50']):
                    self.bot.close_position(self.symbol, "Buy", position_size)
                    logger.info(f"\n[POSITION CLOSED - LONG]")
                    logger.info(f"Time: {datetime.now()}")
                    logger.info(f"Size: {position_size}")
                    
                elif position_side == "Sell" and (analysis['rsi'] < 30 or analysis['sma_20'] > analysis['sma_50']):
                    self.bot.close_position(self.symbol, "Sell", position_size)
                    logger.info(f"\n[POSITION CLOSED - SHORT]")
                    logger.info(f"Time: {datetime.now()}")
                    logger.info(f"Size: {position_size}")
                    
            logger.info("=== EXECUTION COMPLETE ===\n")
                
        except Exception as e:
            logger.error(f"Strategy execution error: {str(e)}")

