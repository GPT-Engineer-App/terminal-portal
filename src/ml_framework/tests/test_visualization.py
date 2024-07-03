import unittest
import numpy as np
import pandas as pd
from ml_framework.visualization import DataVisualizer

class TestDataVisualizer(unittest.TestCase):
    def setUp(self):
        self.visualizer = DataVisualizer()

    def test_plot_correlation_matrix(self):
        data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        })
        self.visualizer.plot_correlation_matrix(data)
        # No assertion, just ensure no exceptions are raised

    def test_plot_feature_importance(self):
        class MockModel:
            feature_importances_ = np.array([0.2, 0.3, 0.5])

        model = MockModel()
        feature_names = ['feature1', 'feature2', 'feature3']
        self.visualizer.plot_feature_importance(model, feature_names)
        # No assertion, just ensure no exceptions are raised

if __name__ == '__main__':
    unittest.main()