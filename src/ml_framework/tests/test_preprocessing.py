import unittest
import numpy as np
from ml_framework.preprocessing import DataPreprocessor

class TestDataPreprocessor(unittest.TestCase):
    def setUp(self):
        self.preprocessor = DataPreprocessor()

    def test_handle_missing_values(self):
        data = np.array([[1, 2], [np.nan, 3], [7, 6]])
        processed_data = self.preprocessor.handle_missing_values(data)
        self.assertFalse(np.isnan(processed_data).any())

    def test_scale_numerical_features(self):
        data = np.array([[1, 2], [3, 4], [5, 6]])
        processed_data = self.preprocessor.scale_numerical_features(data)
        self.assertAlmostEqual(np.mean(processed_data), 0)
        self.assertAlmostEqual(np.std(processed_data), 1)

    def test_encode_categorical_variables(self):
        data = np.array([['cat'], ['dog'], ['cat']])
        processed_data = self.preprocessor.encode_categorical_variables(data)
        self.assertEqual(processed_data.shape[1], 2)

if __name__ == '__main__':
    unittest.main()