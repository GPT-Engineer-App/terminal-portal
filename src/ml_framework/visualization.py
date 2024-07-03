import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self):
        pass

    def plot_correlation_matrix(self, data):
        corr = data.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.show()

    def plot_feature_importance(self, model, feature_names):
        importance = model.feature_importances_
        plt.barh(feature_names, importance)
        plt.xlabel('Feature Importance')
        plt.ylabel('Feature')
        plt.show()