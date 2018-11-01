import unittest

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.cluster import KMeans
from sklearn.svm import SVC

from scikest.estimate import Estimator


class TestEstimate(unittest.TestCase):
    inputs, outputs = None, None

    def setUp(self):
        self.estimator = Estimator(meta_algo='RF', verbose=0)

    def test_fetch_name(self):
        rf = RandomForestRegressor()
        svc = SVC()
        kmeans = KMeans()
        rf_name = self.estimator._fetch_name(rf)
        svc_name = self.estimator._fetch_name(svc)
        kmeans_name = self.estimator._fetch_name(kmeans)
        assert rf_name == 'RandomForestRegressor'
        assert svc_name == 'SVC'
        assert kmeans_name == 'KMeans'


    def test_estimate_duration(self):
        rf = RandomForestRegressor()
        svc = SVC()
        kmeans = KMeans()
        X, y_continuous = np.random.rand(10000, 10), np.random.rand(10000, 1)
        y_class = np.random.randint(0, 4, 10000)
        # run the estimation
        rf_duration = self.estimator.estimate_duration(rf, X, y_continuous)
        svc_duration = self.estimator.estimate_duration(svc, X, y_class)
        kmeans_duration = self.estimator.estimate_duration(kmeans, X)

        assert type(rf_duration[0]) == np.float64
        assert type(svc_duration[0]) == np.float64
        assert type(kmeans_duration[0]) == np.float64


if __name__ == '__main__':
    unittest.main()
