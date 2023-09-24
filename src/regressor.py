from sklearn.dummy import DummyRegressor
import numpy as np

class CustomDummyRegressor(DummyRegressor):

    def fracsum(self, X, y):
        fractional_parts = np.modf(y)[0]
        return np.sum(fractional_parts)