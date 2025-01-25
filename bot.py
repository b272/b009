import time
import hashlib
import hmac
import requests
from urllib.parse import urlencode
import json
import pandas as pd
import numpy as np
from datetime import datetime
from open_close_prices import analyze_open_close_prices
from high_low_prices import analyze_price_extremes
from volume_analysis import analyze_trading_volume

def perform_market_analysis(data):
    results = {
        'price_analysis': analyze_open_close_prices(data),
        'extremes_analysis': analyze_price_extremes(data),
        'volume_analysis': analyze_trading_volume(data)
    }
    return results

class BybitBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api-demo.bybit.com" if testnet else "https://api.bybit.com"

    def get_available_pairs(self):
        endpoint = "/v5/market/instruments-info"
        params = "category=linear"
        timestamp = str(int(time.time() * 1000))
        signature = self.generate_signature(params, timestamp)
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

    def check_api_access(self):
        print("Starting API access verification...")
        
        balance = self.get_balance()
        print("\nWallet Balance:")
        if balance.get('retCode') == 0:
            for coin in balance['result']['list'][0]['coin']:
                print(f"{coin['coin']}: {coin['walletBalance']}")
        print("\nBalance access:", "Success" if balance.get('retCode') == 0 else "Failed")
        
        test_order = self.place_order(
            symbol="BTCUSDT",
            side="Buy",
            order_type="Limit",
            qty=0.001,
            price=1
        )
        print("Order access:", "Success" if test_order.get('retCode') in [0, 110003] else "Failed")
        
        return balance.get('retCode') == 0 and test_order.get('retCode') in [0, 110003]

    def generate_signature(self, params, timestamp):
        param_str = str(timestamp) + self.api_key + "5000" + params
        return hmac.new(
            self.api_secret.encode('utf-8'),
            param_str.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def get_balance(self):
        endpoint = "/v5/account/wallet-balance"
        timestamp = str(int(time.time() * 1000))
        params = "accountType=UNIFIED"
        signature = self.generate_signature(params, timestamp)
        headers = {
            "X-BAPI-API-KEY": self.api_key,
            "X-BAPI-SIGN": signature,
            "X-BAPI-TIMESTAMP": timestamp,
            "X-BAPI-RECV-WINDOW": "5000",
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + endpoint + "?" + params,
            headers=headers
        )
        return response.json()

    def place_order(self, symbol, side, order_type, qty, price=None):
        endpoint = "/v5/order/create"
        timestamp = str(int(time.time() * 1000))
        params = {
            "category": "linear",
            "symbol": symbol,
            "side": side,
            "orderType": order_type,
            "qty": str(qty),
            "timeInForce": "GTC"
        }
        if price:
            params["price"] = str(price)
        params_str = json.dumps(params)
        signature = self.generate_signature(params_str, timestamp)
        headers = {
            "X-BAPI-API-KEY": self.api_key,
            "X-BAPI-SIGN": signature,
            "X-BAPI-TIMESTAMP": timestamp,
            "X-BAPI-RECV-WINDOW": "5000",
            "Content-Type": "application/json"
        }
        response = requests.post(
            self.base_url + endpoint,
            headers=headers,
            json=params
        )
        return response.json()

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

    def get_klines(self):
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

    def calculate_rsi(self, prices, period=14):
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def analyze_market(self):
        klines = self.get_klines()
        df = pd.DataFrame(klines['result']['list'])
        df['close'] = pd.to_numeric(df[4])
        df['rsi'] = self.calculate_rsi(df['close'], self.rsi_period)
        df['sma_20'] = df['close'].rolling(window=20).mean()
        df['sma_50'] = df['close'].rolling(window=50).mean()
        latest_data = df.iloc[-1]
        return {
            'rsi': latest_data['rsi'],
            'sma_20': latest_data['sma_20'],
            'sma_50': latest_data['sma_50'],
            'close': latest_data['close']
        }

    def get_position(self):
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
        current_data = self.analyze_market()
        position_data = self.get_position()
        
        rsi = current_data['rsi']
        sma_20 = current_data['sma_20']
        sma_50 = current_data['sma_50']
        
        has_position = len(position_data['result']['list']) > 0
        
        if not has_position:
            if rsi < 30 and sma_20 > sma_50:
                self.bot.place_order(
                    symbol=self.symbol,
                    side="Buy",
                    order_type="Market",
                    qty=0.001
                )
            elif rsi > 70 and sma_20 < sma_50:
                self.bot.place_order(
                    symbol=self.symbol,
                    side="Sell",
                    order_type="Market",
                    qty=0.001
                )
        else:
            current_position = position_data['result']['list'][0]
            position_size = abs(float(current_position['size']))
            position_side = current_position['side']
            
            if position_side == "Buy":
                if rsi > 70 or sma_20 < sma_50:
                    self.bot.place_order(
                        symbol=self.symbol,
                        side="Sell",
                        order_type="Market",
                        qty=position_size
                    )
            else:
                if rsi < 30 or sma_20 > sma_50:
                    self.bot.place_order(
                        symbol=self.symbol,
                        side="Buy",
                        order_type="Market",
                        qty=position_size
                    )

def run_bot():
    api_key = "ho4zFTq8bbyWCGNN24"
    api_secret = "PSjYZzt4UtdvTE8ziNpoPS4cwUNwwfUIXeV4"
    
    temp_bot = BybitBot(api_key, api_secret)
    pairs = temp_bot.get_available_pairs()
    
    print("\nAvailable trading pairs:")
    for i, pair in enumerate(pairs['result']['list'], 1):
        print(f"{i}. {pair['symbol']}")
    
    while True:
        try:
            choice = int(input("\nSelect trading pair number: ")) - 1
            selected_pair = pairs['result']['list'][choice]['symbol']
            break
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")
    
    print(f"\nSelected trading pair: {selected_pair}")
    
    trading_logic = TradingLogic(api_key, api_secret, symbol=selected_pair)
    
    if trading_logic.bot.check_api_access():
        print("API verification successful! Starting trading bot...")
        while True:
            try:
                trading_logic.execute_strategy()
                print(f"Strategy executed at {datetime.now()}")
                time.sleep(60)
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(60)
    else:
        print("API verification failed. Please check your credentials and permissions.")

if __name__ == "__main__":
    run_bot()
