import unittest
import numpy as np
from sklearn.linear_model import LogisticRegression as SklearnLogisticRegression
from ml_framework.tuning import HyperparameterTuner

class TestHyperparameterTuner(unittest.TestCase):
    def setUp(self):
        self.model = SklearnLogisticRegression()
        self.param_grid = {'C': [0.1, 1, 10]}
        self.tuner = HyperparameterTuner(self.model, self.param_grid)

    def test_tune(self):
        X = np.array([[1], [2], [3], [4]])
        y = np.array([0, 0, 1, 1])
        best_params, best_score = self.tuner.tune(X, y)
        self.assertIn(best_params['C'], [0.1, 1, 10])
        self.assertGreaterEqual(best_score, 0)

if __name__ == '__main__':
    unittest.main()