import pandas as pd
import numpy as np

def analyze_trading_volume(data):
    """
    Analyzes trading volume patterns and indicators
    
    Parameters:
        data (pd.DataFrame): DataFrame containing OHLCV data
        
    Returns:
        dict: Volume analysis metrics and patterns
    """
    df = pd.DataFrame(data)
    df['volume'] = pd.to_numeric(df[5])
    df['close'] = pd.to_numeric(df[4])
    
    results = {
        'volume_metrics': calculate_volume_metrics(df),
        'volume_trends': analyze_volume_trends(df),
        'price_volume_correlation': analyze_price_volume_correlation(df),
        'volume_indicators': calculate_volume_indicators(df),
        'volume_patterns': identify_volume_patterns(df)
    }
    
    return results

def calculate_volume_metrics(df, period=20):
    """
    Calculates key volume metrics
    """
    avg_volume = df['volume'].rolling(window=period).mean()
    relative_volume = df['volume'] / avg_volume
    
    return {
        'current_volume': df['volume'].iloc[-1],
        'average_volume': avg_volume.iloc[-1],
        'relative_volume': relative_volume.iloc[-1],
        'volume_std': df['volume'].rolling(window=period).std().iloc[-1]
    }

def analyze_volume_trends(df, period=20):
    """
    Analyzes volume trends and momentum
    """
    volume_sma = df['volume'].rolling(window=period).mean()
    volume_momentum = df['volume'].diff(period)
    
    trend = 'Increasing' if volume_momentum.iloc[-1] > 0 else 'Decreasing'
    
    return {
        'volume_trend': trend,
        'volume_momentum': volume_momentum.iloc[-1],
        'above_average': df['volume'].iloc[-1] > volume_sma.iloc[-1]
    }

def analyze_price_volume_correlation(df, period=20):
    """
    Analyzes correlation between price and volume
    """
    price_changes = df['close'].pct_change()
    volume_changes = df['volume'].pct_change()
    
    correlation = price_changes.rolling(window=period).corr(volume_changes)
    
    return {
        'price_volume_correlation': correlation.iloc[-1],
        'volume_price_ratio': df['volume'].iloc[-1] / df['close'].iloc[-1]
    }

def calculate_volume_indicators(df):
    """
    Calculates various volume-based indicators
    """
    # On-Balance Volume (OBV)
    df['price_change'] = df['close'].diff()
    df['obv'] = (df['volume'] * (df['price_change'].apply(lambda x: 1 if x > 0 else -1 if x < 0 else 0))).cumsum()
    
    # Volume Force Index
    df['force_index'] = df['price_change'] * df['volume']
    
    # Money Flow Index components
    typical_price = (df['high'] + df['low'] + df['close']) / 3
    money_flow = typical_price * df['volume']
    
    return {
        'obv': df['obv'].iloc[-1],
        'force_index': df['force_index'].iloc[-1],
        'money_flow': money_flow.iloc[-1]
    }

def identify_volume_patterns(df, threshold=1.5):
    """
    Identifies specific volume patterns
    """
    patterns = []
    avg_volume = df['volume'].rolling(window=20).mean()
    
    # Volume Spike
    if df['volume'].iloc[-1] > avg_volume.iloc[-1] * threshold:
        patterns.append('Volume Spike')
    
    # Volume Climax
    if len(df) >= 3:
        if (df['volume'].iloc[-1] > df['volume'].iloc[-2] > df['volume'].iloc[-3]):
            patterns.append('Rising Volume')
        elif (df['volume'].iloc[-1] < df['volume'].iloc[-2] < df['volume'].iloc[-3]):
            patterns.append('Falling Volume')
    
    # Price/Volume Divergence
    price_trend = df['close'].diff().iloc[-1]
    volume_trend = df['volume'].diff().iloc[-1]
    
    if price_trend > 0 and volume_trend < 0:
        patterns.append('Bearish Divergence')
    elif price_trend < 0 and volume_trend > 0:
        patterns.append('Bullish Divergence')
        
    return patterns

def calculate_volume_profile(df, price_levels=10):
    """
    Creates volume profile analysis
    """
    price_bins = pd.qcut(df['close'], q=price_levels, duplicates='drop')
    volume_profile = df.groupby(price_bins)['volume'].sum()
    
    return {
        'volume_by_price': volume_profile.to_dict(),
        'poc_price': volume_profile.idxmax().left  # Point of Control
    }
