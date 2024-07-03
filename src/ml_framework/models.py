import numpy as np

class LinearRegression:
    def __init__(self):
        self.weights = None

    def fit(self, X, y):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        self.weights = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

    def predict(self, X):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        return X_b.dot(self.weights)

class LogisticRegression:
    def __init__(self):
        self.weights = None

    def fit(self, X, y, lr=0.01, epochs=1000):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        self.weights = np.zeros(X_b.shape[1])
        for _ in range(epochs):
            gradients = X_b.T.dot(self._sigmoid(X_b.dot(self.weights)) - y) / y.size
            self.weights -= lr * gradients

    def predict(self, X):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        return self._sigmoid(X_b.dot(self.weights)) >= 0.5

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

class DecisionTree:
    def __init__(self):
        pass  # Placeholder for decision tree implementation

    def fit(self, X, y):
        pass  # Placeholder for fit method

    def predict(self, X):
        pass  # Placeholder for predict method

class NeuralNetwork:
    def __init__(self):
        pass  # Placeholder for neural network implementation

    def fit(self, X, y):
        pass  # Placeholder for fit method

    def predict(self, X):
        pass  # Placeholder for predict method