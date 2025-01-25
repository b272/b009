import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

class PricePredictor:
    def __init__(self, lookback_period=60):
        self.lookback = lookback_period
        self.scaler = MinMaxScaler()
        self.model = self._build_model()
        
    def _build_model(self):
        """Build LSTM model architecture"""
        model = Sequential([
            LSTM(units=50, return_sequences=True, input_shape=(self.lookback, 1)),
            Dropout(0.2),
            LSTM(units=50, return_sequences=False),
            Dropout(0.2),
            Dense(units=1)
        ])
        model.compile(optimizer='adam', loss='mse')
        return model
        
    def prepare_data(self, df):
        """Prepare data for LSTM model"""
        # Create features
        df['returns'] = df['close'].pct_change()
        df['volatility'] = df['returns'].rolling(window=20).std()
        df['momentum'] = df['close'] - df['close'].shift(20)
        
        # Scale features
        features = ['close', 'volume', 'returns', 'volatility', 'momentum']
        scaled_data = self.scaler.fit_transform(df[features])
        
        X, y = [], []
        for i in range(self.lookback, len(scaled_data)):
            X.append(scaled_data[i-self.lookback:i])
            y.append(scaled_data[i, 0])
            
        return np.array(X), np.array(y)
        
    def train(self, df, epochs=50, batch_size=32):
        """Train the model"""
        X, y = self.prepare_data(df)
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size, verbose=1)
        
    def predict_next(self, df):
        """Predict next price movement"""
        X, _ = self.prepare_data(df.tail(self.lookback + 1))
        prediction = self.model.predict(X[-1:])
        return self.scaler.inverse_transform(prediction)[0][0]

# Integration with trading logic
def enhance_trading_logic():
    """Add ML predictions to trading decisions"""
    predictor = PricePredictor()
    
    def predict_price_movement(df):
        """Get price movement prediction"""
        current_price = df['close'].iloc[-1]
        predicted_price = predictor.predict_next(df)
        movement = (predicted_price - current_price) / current_price * 100
        
        return {
            'direction': 'up' if movement > 0 else 'down',
            'magnitude': abs(movement),
            'confidence': calculate_prediction_confidence(df)
        }
        
    def calculate_prediction_confidence(df):
        """Calculate confidence score for prediction"""
        volatility = df['close'].pct_change().std()
        volume_trend = df['volume'].tail(20).mean() > df['volume'].tail(50).mean()
        trend_strength = abs(df['close'].tail(20).mean() - df['close'].tail(50).mean())
        
        confidence = 0.5  # Base confidence
        confidence += 0.2 if volatility < 0.02 else -0.1  # Lower volatility = higher confidence
        confidence += 0.15 if volume_trend else -0.05  # Rising volume = higher confidence
        confidence += 0.15 if trend_strength > 100 else 0  # Strong trend = higher confidence
        
        return min(max(confidence, 0), 1)  # Ensure confidence is between 0 and 1

    return predict_price_movement
