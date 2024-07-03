import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

class DataPreprocessor:
    def __init__(self):
        self.imputer = SimpleImputer(strategy='mean')
        self.scaler = StandardScaler()
        self.encoder = OneHotEncoder(sparse=False)

    def handle_missing_values(self, data):
        return self.imputer.fit_transform(data)

    def scale_numerical_features(self, data):
        return self.scaler.fit_transform(data)

    def encode_categorical_variables(self, data):
        return self.encoder.fit_transform(data)