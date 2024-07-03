from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

class HyperparameterTuner:
    def __init__(self, model, param_grid, search_type='grid'):
        self.model = model
        self.param_grid = param_grid
        self.search_type = search_type

    def tune(self, X, y):
        if self.search_type == 'grid':
            search = GridSearchCV(self.model, self.param_grid, cv=5)
        else:
            search = RandomizedSearchCV(self.model, self.param_grid, cv=5)
        search.fit(X, y)
        return search.best_params_, search.best_score_