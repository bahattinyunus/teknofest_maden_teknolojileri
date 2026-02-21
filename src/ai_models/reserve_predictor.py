import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

class ReservePredictor:
    """
    A class to predict mineral reserves based on geological data using AI models (GPR and Neural Networks).
    """
    def __init__(self, model_path=None):
        # Neural Network for large-scale patterns
        if model_path:
            self.nn_model = keras.models.load_model(model_path)
            print(f"NN Model loaded from {model_path}")
        else:
            self.nn_model = self._build_nn_model()
            print("New NN model initialized.")
        
        # Gaussian Process for spatial uncertainty and refinement (Maden Teknolojileri Special)
        kernel = C(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2))
        self.gpr_model = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
        self.gpr_fitted = False

    def _build_nn_model(self):
        """
        Builds a neural network model for broad pattern recognition.
        """
        model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=(12,)), # 10 features + 2 (X,Y) coords
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(1, activation='linear')
        ])
        model.compile(optimizer='adam', loss='mse')
        return model

    def train(self, X, y):
        """
        Trains both NN and GPR models. 
        X should include features and (X, Y) coordinates.
        """
        print("Training Neural Network...")
        self.nn_model.fit(X, y, epochs=20, verbose=0)
        
        print("Fitting Gaussian Process Regressor...")
        # GPR is computationally expensive, use a subset if data is huge
        self.gpr_model.fit(X, y)
        self.gpr_fitted = True
        print("Training complete.")

    def predict(self, X):
        """
        Hybrid prediction: NN prediction + GPR refinement.
        """
        nn_pred = self.nn_model.predict(X).flatten()
        
        if self.gpr_fitted:
            gpr_pred, sigma = self.gpr_model.predict(X, return_std=True)
            # Weighted average or simple addition of residual prediction
            # Here we use NN as base and GPR for local refinement
            return (nn_pred + gpr_pred) / 2, sigma
        
        return nn_pred, None

    def generate_geological_data(self, samples=100):
        """
        Generates realistic synthetic geological data with spatial correlation.
        """
        # (X, Y) Coordinates (0 to 1000m)
        coords = np.random.rand(samples, 2) * 1000
        # 10 other geological features (density, depth, mineralization etc.)
        features = np.random.rand(samples, 10)
        
        X = np.hstack([coords, features])
        
        # Target: Reserve amount based on coords and features
        # Creating a 'hotspot' at (500, 500)
        dist_from_hotspot = np.linalg.norm(coords - [500, 500], axis=1)
        hotspot_effect = 500 * np.exp(-dist_from_hotspot / 250)
        
        y = hotspot_effect + np.sum(features, axis=1) * 50 + np.random.normal(0, 5, samples)
        return X, y

def main():
    predictor = ReservePredictor()
    X_train, y_train = predictor.generate_geological_data(300)
    predictor.train(X_train, y_train)
    
    X_test, y_test = predictor.generate_geological_data(10)
    predictions, sigmas = predictor.predict(X_test)
    
    print("\n--- Project DeepMine AI: Reserve Estimation Results ---")
    for i in range(len(predictions)):
        uncertainty = f" (Uncertainty: ±{sigmas[i]:.2f})" if sigmas is not None else ""
        print(f"Site {i+1} [Coord: {X_test[i,0]:.1f}, {X_test[i,1]:.1f}] -> Est: {predictions[i]:.2f} tons{uncertainty}")

if __name__ == "__main__":
    main()
