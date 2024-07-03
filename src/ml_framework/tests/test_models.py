import unittest
import numpy as np
from ml_framework.models import LinearRegression, LogisticRegression

class TestLinearRegression(unittest.TestCase):
    def setUp(self):
        self.model = LinearRegression()

    def test_fit_and_predict(self):
        X = np.array([[1], [2], [3], [4]])
        y = np.array([2, 3, 4, 5])
        self.model.fit(X, y)
        predictions = self.model.predict(X)
        self.assertTrue(np.allclose(predictions, y))

class TestLogisticRegression(unittest.TestCase):
    def setUp(self):
        self.model = LogisticRegression()

    def test_fit_and_predict(self):
        X = np.array([[1], [2], [3], [4]])
        y = np.array([0, 0, 1, 1])
        self.model.fit(X, y)
        predictions = self.model.predict(X)
        self.assertTrue(np.array_equal(predictions, y))

if __name__ == '__main__':
    unittest.main()