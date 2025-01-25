import pandas as pd
import numpy as np

def analyze_open_close_prices(data):
    """
    Analyzes open and close prices to identify price patterns and trends
    
    Parameters:
        data (pd.DataFrame): DataFrame containing OHLCV data
        
    Returns:
        dict: Analysis results including price trends and patterns
    """
    df = pd.DataFrame(data)
    df['open'] = pd.to_numeric(df[1])
    df['close'] = pd.to_numeric(df[4])
    
    # Calculate price changes
    df['price_change'] = df['close'] - df['open']
    df['price_change_pct'] = (df['price_change'] / df['open']) * 100
    
    # Identify bullish and bearish candles
    df['is_bullish'] = df['close'] > df['open']
    
    # Calculate moving averages
    df['sma_20'] = df['close'].rolling(window=20).mean()
    df['sma_50'] = df['close'].rolling(window=50).mean()
    
    # Trend analysis
    current_trend = 'Bullish' if df['sma_20'].iloc[-1] > df['sma_50'].iloc[-1] else 'Bearish'
    
    # Calculate consecutive candles
    consecutive_bullish = count_consecutive_candles(df['is_bullish'], True)
    consecutive_bearish = count_consecutive_candles(df['is_bullish'], False)
    
    results = {
        'current_trend': current_trend,
        'price_change_24h': df['price_change'].iloc[-1],
        'price_change_pct_24h': df['price_change_pct'].iloc[-1],
        'consecutive_bullish': consecutive_bullish,
        'consecutive_bearish': consecutive_bearish,
        'average_daily_range': calculate_average_range(df),
        'trend_strength': calculate_trend_strength(df)
    }
    
    return results

def count_consecutive_candles(series, condition):
    """
    Counts consecutive candles meeting a condition
    """
    count = 0
    for value in reversed(series):
        if value == condition:
            count += 1
        else:
            break
    return count

def calculate_average_range(df, period=14):
    """
    Calculates the average daily price range
    """
    daily_range = abs(df['close'] - df['open'])
    return daily_range.rolling(window=period).mean().iloc[-1]

def calculate_trend_strength(df, period=14):
    """
    Calculates trend strength using price momentum
    """
    momentum = df['close'].diff(period)
    strength = abs(momentum.iloc[-1]) / df['close'].iloc[-1] * 100
    return strength

def get_price_patterns(df):
    """
    Identifies common price patterns
    """
    patterns = []
    
    # Doji pattern
    df['doji'] = abs(df['close'] - df['open']) <= (df['high'] - df['low']) * 0.1
    
    # Engulfing pattern
    df['bullish_engulfing'] = (df['open'].shift(1) > df['close'].shift(1)) & \
                             (df['close'] > df['open']) & \
                             (df['open'] <= df['close'].shift(1)) & \
                             (df['close'] >= df['open'].shift(1))
                             
    df['bearish_engulfing'] = (df['close'].shift(1) > df['open'].shift(1)) & \
                             (df['open'] > df['close']) & \
                             (df['close'] <= df['open'].shift(1)) & \
                             (df['open'] >= df['close'].shift(1))
    
    if df['doji'].iloc[-1]:
        patterns.append('Doji')
    if df['bullish_engulfing'].iloc[-1]:
        patterns.append('Bullish Engulfing')
    if df['bearish_engulfing'].iloc[-1]:
        patterns.append('Bearish Engulfing')
        
    return patterns
