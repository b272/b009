import pandas as pd
import numpy as np
from datetime import datetime

def perform_market_analysis(data):
    """
    Comprehensive market analysis combining price, volume and trend data
    
    Parameters:
        data (dict): Market data from exchange
        
    Returns:
        dict: Combined analysis results
    """
    df = pd.DataFrame(data['result']['list'])
    df['open'] = pd.to_numeric(df[1])
    df['high'] = pd.to_numeric(df[2]) 
    df['low'] = pd.to_numeric(df[3])
    df['close'] = pd.to_numeric(df[4])
    df['volume'] = pd.to_numeric(df[5])

    results = {
        'price_analysis': analyze_price_action(df),
        'trend_analysis': analyze_trends(df),
        'volume_analysis': analyze_volume(df),
        'volatility': calculate_volatility(df),
        'support_resistance': find_key_levels(df)
    }
    
    return results

def analyze_price_action(df):
    """Analyze price action patterns"""
    return {
        'last_close': df['close'].iloc[-1],
        'daily_change': (df['close'].iloc[-1] - df['open'].iloc[-1]) / df['open'].iloc[-1] * 100,
        'price_momentum': df['close'].diff().iloc[-1],
        'avg_range': (df['high'] - df['low']).mean()
    }

def analyze_trends(df):
    """Analyze market trends"""
    sma_20 = df['close'].rolling(window=20).mean()
    sma_50 = df['close'].rolling(window=50).mean()
    
    return {
        'trend': 'Bullish' if sma_20.iloc[-1] > sma_50.iloc[-1] else 'Bearish',
        'trend_strength': abs(sma_20.iloc[-1] - sma_50.iloc[-1]) / sma_50.iloc[-1] * 100,
        'momentum': calculate_momentum(df)
    }

def analyze_volume(df):
    """Analyze trading volume"""
    avg_volume = df['volume'].rolling(window=20).mean()
    
    return {
        'current_volume': df['volume'].iloc[-1],
        'avg_volume': avg_volume.iloc[-1],
        'volume_trend': 'Increasing' if df['volume'].iloc[-1] > avg_volume.iloc[-1] else 'Decreasing',
        'volume_momentum': df['volume'].diff().iloc[-1]
    }

def calculate_volatility(df, window=14):
    """Calculate market volatility"""
    returns = df['close'].pct_change()
    volatility = returns.std() * np.sqrt(252) * 100
    
    atr = calculate_atr(df, window)
    
    return {
        'volatility': volatility,
        'atr': atr,
        'volatility_state': 'High' if volatility > returns.std() * 2 else 'Normal'
    }

def calculate_atr(df, window):
    """Calculate Average True Range"""
    tr = pd.DataFrame()
    tr['h-l'] = df['high'] - df['low']
    tr['h-pc'] = abs(df['high'] - df['close'].shift())
    tr['l-pc'] = abs(df['low'] - df['close'].shift())
    tr['tr'] = tr[['h-l', 'h-pc', 'l-pc']].max(axis=1)
    atr = tr['tr'].rolling(window=window).mean()
    
    return atr.iloc[-1]

def calculate_momentum(df, period=14):
    """Calculate price momentum"""
    momentum = df['close'].diff(period)
    return momentum.iloc[-1]

def find_key_levels(df):
    """Find support and resistance levels"""
    pivot = (df['high'].iloc[-1] + df['low'].iloc[-1] + df['close'].iloc[-1]) / 3
    
    return {
        'pivot': pivot,
        'support_1': 2 * pivot - df['high'].iloc[-1],
        'resistance_1': 2 * pivot - df['low'].iloc[-1],
        'daily_range': df['high'].iloc[-1] - df['low'].iloc[-1]
    }
