import numpy as np
import tensorflow as tf
from tensorflow import keras

class ReservePredictor:
    """
    A class to predict mineral reserves based on geological data using AI models.
    """
    def __init__(self, model_path=None):
        if model_path:
            self.model = keras.models.load_model(model_path)
            print(f"Model loaded from {model_path}")
        else:
            self.model = self._build_model()
            print("New model initialized.")

    def _build_model(self):
        """
        Builds a simple neural network model for demonstration purposes.
        """
        model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=(10,)), # Example input size
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(1, activation='linear') # Regression output for reserve quantity
        ])
        model.compile(optimizer='adam', loss='mse')
        return model

    def predict_reserve(self, geological_data):
        """
        Predicts the reserve amount based on input geological data.
        
        Args:
            geological_data (np.array): Input features for prediction.
            
        Returns:
            float: Predicted reserve amount.
        """
        if self.model is None:
            raise ValueError("Model not initialized.")
        
        prediction = self.model.predict(geological_data)
        return prediction

if __name__ == "__main__":
    # Example usage
    predictor = ReservePredictor()
    dummy_data = np.random.rand(1, 10)
    prediction = predictor.predict_reserve(dummy_data)
    print(f"Predicted Reserve: {prediction[0][0]:.2f} tons")
