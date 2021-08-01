from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

from sklearn.datasets import load_iris
class MachineLearningCode:
    def __init__(self):
        self.iris = load_iris()
        self.knn=None
        self.X_new = None
        self.X_train=None
        self.X_test=None
        self.y_train=None
        self.y_test=None
        self.prediction=None
    def train(self):
        # Split our dataset into training and testing sets.
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.iris['data'], self.iris['target'], random_state=0)
        self.knn = KNeighborsClassifier(n_neighbors=1)
        self.knn.fit(self.X_train, self.y_train)

    # Imagine that we obtained a new iris
    def predict(self,sl,sw,pl,pw):
        self.X_new = np.array([[sl, sw, pl, pw]])
        print(self.X_new.shape)
        self.prediction = self.knn.predict(self.X_new)
        # print(self.prediction)
        return [(self.iris['target_names'][self.prediction]),(self.knn.score(self.X_test, self.y_test))]