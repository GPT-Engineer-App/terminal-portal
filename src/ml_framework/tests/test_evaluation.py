import unittest
import numpy as np
from ml_framework.evaluation import ModelEvaluator

class TestModelEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = ModelEvaluator()

    def test_evaluate_classification(self):
        y_true = np.array([0, 1, 0, 1])
        y_pred = np.array([0, 1, 0, 0])
        accuracy = self.evaluator.evaluate_classification(y_true, y_pred)
        self.assertEqual(accuracy, 0.75)

    def test_evaluate_regression(self):
        y_true = np.array([1.0, 2.0, 3.0, 4.0])
        y_pred = np.array([1.1, 1.9, 3.2, 3.8])
        mse = self.evaluator.evaluate_regression(y_true, y_pred)
        self.assertAlmostEqual(mse, 0.015)

if __name__ == '__main__':
    unittest.main()