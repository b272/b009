import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # API Configuration
    API_KEY = "ho4zFTq8bbyWCGNN24"
    API_SECRET = "PSjYZzt4UtdvTE8ziNpoPS4cwUNwwfUIXeV4"
    TESTNET = os.getenv('USE_TESTNET', 'True').lower() == 'true'

    # Trading Parameters - Optimized for Active Trading
    DEFAULT_SYMBOL = 'BTCUSDT'
    TIMEFRAME = '5'  
    QUANTITY = 0.002  # Increased for better profit potential

    # Technical Analysis - More Dynamic Settings
    RSI_PERIOD = 14
    RSI_OVERBOUGHT = 80  # Expanded range for trend riding
    RSI_OVERSOLD = 20    # Expanded range for trend riding
    SMA_FAST = 3         # Faster trend detection
    SMA_SLOW = 13        # Better medium-term trend signals

    # Risk Management - Optimized Risk/Reward
    MAX_POSITION_SIZE = 0.02    # Larger position sizing
    STOP_LOSS_PCT = 0.04       # 3% stop loss
    TAKE_PROFIT_PCT = 0.06     # 6% take profit
    MAX_DAILY_TRADES = 15      # More trading opportunities
    
    # Logging Configuration
    LOG_LEVEL = 'INFO'
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_FILE = 'logs/trading.log'
    
    # Database Configuration
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', 5432))
    DB_NAME = os.getenv('DB_NAME', 'trading_bot')
    DB_USER = os.getenv('DB_USER', 'user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    
    # Webhook Notifications
    DISCORD_WEBHOOK = os.getenv('DISCORD_WEBHOOK', '')
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')
    
    # Performance Tracking
    TRACK_PERFORMANCE = True
    PERFORMANCE_METRICS = [
        'win_rate',
        'profit_factor',
        'sharpe_ratio',
        'max_drawdown'
    ]
    
    # Market Hours
    TRADING_HOURS = {
        'start': '00:00',
        'end': '23:59'
    }
    
    # Strategy Parameters
    STRATEGY_PARAMS = {
        'min_volume': 1000000,
        'min_volatility': 0.02,
        'trend_strength': 0.5
    }
    
    @staticmethod
    def get_db_url():
        return f"postgresql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
    
    @staticmethod
    def validate_config():
        """Validates critical configuration parameters"""
        required_vars = [
            'API_KEY',
            'API_SECRET',
            'DEFAULT_SYMBOL'
        ]
        
        for var in required_vars:
            if not getattr(Config, var):
                raise ValueError(f"Missing required configuration: {var}")
        
        return True

class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = 'DEBUG'
    TESTNET = True

class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = 'INFO'
    TESTNET = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    LOG_LEVEL = 'DEBUG'
    TESTNET = True
