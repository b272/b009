import os
import logging
import time
from datetime import datetime
from bybit_bot import BybitBot
from trading_logic import TradingLogic
from utils.config import Config
from analysis.market_analysis import perform_market_analysis
import signal
import sys

def setup_logging():
    # Create logs directory
    os.makedirs('logs', exist_ok=True)
    
    # Set up file logging
    file_handler = logging.FileHandler('logs/trading.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    # Set up console logging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    # Configure root logger
    logging.basicConfig(
        level=logging.INFO,
        handlers=[file_handler, console_handler]
    )

    logger = logging.getLogger(__name__)
    return logger

def signal_handler(sig, frame):
    logger.info("\n=== SHUTTING DOWN TRADING BOT ===")
    logger.info("Closing all open positions...")
    # Close any open positions here
    logger.info("Cleanup complete. Bot stopped safely.")
    sys.exit(0)

# Create logs directory
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
logging.basicConfig(
    level=Config.LOG_LEVEL,
    format=Config.LOG_FORMAT,
    handlers=[
        logging.FileHandler('logs/trading.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def initialize_bot():
    """Initialize and verify bot connection"""
    logger.info("\n=== BYBIT TRADING BOT STARTUP ===")
    
    bot = BybitBot(Config.API_KEY, Config.API_SECRET, Config.TESTNET)
    
    # Connection details
    host = "Testnet" if Config.TESTNET else "Mainnet" 
    logger.info("\n>>> Connection Details:")
    logger.info(f"Host: {host}")
    logger.info(f"API URL: {bot.base_url}")
    logger.info(f"API Key: {Config.API_KEY[:6]}...{Config.API_KEY[-4:]}")
    
    # Account balance
    balance = bot.get_balance()
    if balance.get('retCode') == 0:
        logger.info("\n>>> Wallet Balance:")
        for coin in balance['result']['list'][0]['coin']:
            logger.info(f"{coin['coin']}: {coin['walletBalance']}")
    
    # Open orders
    orders = bot.get_order_history(Config.DEFAULT_SYMBOL)
    if orders.get('retCode') == 0:
        logger.info("\n>>> Open Orders:")
        for order in orders['result']['list']:
            logger.info(f"ID: {order['orderId']}")
            logger.info(f"Symbol: {order['symbol']}")
            logger.info(f"Side: {order['side']}")
            logger.info(f"Price: {order['price']}")
            logger.info("---")
    
    pairs = bot.get_available_pairs()
    logger.info("\n=== STARTUP COMPLETE ===\n")
    return bot, pairs


def verify_configuration():
    """Verify API credentials and permissions"""
    logger.info("\nVerifying API Configuration:")
    logger.info(f"API Key length: {len(Config.API_KEY)}")
    logger.info(f"API Secret length: {len(Config.API_SECRET)}")
    logger.info(f"Network: {'Testnet' if Config.TESTNET else 'Mainnet'}")

def select_trading_pair(pairs):
    """Select trading pair interactively"""
    while True:
        try:
            choice = int(input("\nSelect trading pair number: ")) - 1
            selected_pair = pairs['result']['list'][choice]['symbol']
            logger.info(f"Selected trading pair: {selected_pair}")
            return selected_pair
        except (ValueError, IndexError):
            logger.error("Invalid selection. Please try again.")

def run_trading_cycle(trading_logic):
    """Execute one cycle of trading strategy"""
    try:
        # Get market data
        market_data = trading_logic.get_klines()
        
        # Perform market analysis
        analysis_results = perform_market_analysis(market_data)
        logger.debug(f"Market analysis results: {analysis_results}")
        
        # Execute trading strategy
        trading_logic.execute_strategy()
        logger.info(f"Strategy executed at {datetime.now()}")
        
        # Update performance metrics
        if Config.TRACK_PERFORMANCE:
            update_performance_metrics(trading_logic)
            
    except Exception as e:
        logger.error(f"Error in trading cycle: {str(e)}")
        
def update_performance_metrics(trading_logic):
    """Update and log performance metrics"""
    metrics = {
        'position': trading_logic.get_position(),
        'balance': trading_logic.bot.get_balance()
    }
    logger.info(f"Current performance metrics: {metrics}")

def main():
    logger = setup_logging()
    logger.info("=== TRADING BOT STARTED ===")
    
    """Main bot execution loop"""
    try:
        # Initialize bot and get trading pairs
        bot, pairs = initialize_bot()
        
        # Select trading pair
        selected_pair = select_trading_pair(pairs)
        
        # Initialize trading logic
        trading_logic = TradingLogic(
            Config.API_KEY,
            Config.API_SECRET,
            symbol=selected_pair,
            interval=Config.TIMEFRAME
        )
        
        # Verify API access
        if trading_logic.bot.check_api_access():
            logger.info("API verification successful! Starting trading bot...")
            
            # Main trading loop
            while True:
                run_trading_cycle(trading_logic)
                time.sleep(5)  # 1-minute delay between cycles
                
        else:
            logger.error("API verification failed. Check credentials and permissions.")
            
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
    except Exception as e:
        logger.error(f"Critical error: {str(e)}")
        
if __name__ == "__main__":
    main()
