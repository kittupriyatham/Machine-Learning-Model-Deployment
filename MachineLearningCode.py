"""
docstring
"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import numpy as np

class MachineLearningCode:
    """
    docstring
    """
    def __init__(self):
        self.iris = load_iris()
        self.knn = None
        self.x_new = None
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None
        self.prediction = None

    def train(self):
        """
        docstring
        """
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            self.iris['data'], self.iris['target'], random_state=0)
        self.knn = KNeighborsClassifier(n_neighbors=1)
        self.knn.fit(self.x_train, self.y_train)

    # Imagine that we obtained a new iris
    def predict(self, sepal_length, sepal_width, petal_length, petal_width):
        """
        docstring
        """
        self.x_new = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        self.prediction = self.knn.predict(self.x_new)
        return [(self.iris['target_names'][self.prediction]), (self.knn.score(
            self.x_test, self.y_test))]
