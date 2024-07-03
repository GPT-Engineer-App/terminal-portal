from sklearn.metrics import accuracy_score, mean_squared_error

class ModelEvaluator:
    def __init__(self):
        pass

    def evaluate_classification(self, y_true, y_pred):
        return accuracy_score(y_true, y_pred)

    def evaluate_regression(self, y_true, y_pred):
        return mean_squared_error(y_true, y_pred)