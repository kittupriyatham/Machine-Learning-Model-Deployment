from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import numpy as np


class MachineLearningCode:
    def __init__(self):
        self.iris = load_iris()
        self.knn = None
        self.X_new = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.prediction = None
        print("Machine Learning Code initialized with None values")

    def train(self):
        print("in train function")
        # Split our dataset into training and testing sets.
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.iris['data'], self.iris['target'],
                                                                                random_state=0)
        print("Splitting data into training and testing sets")
        self.knn = KNeighborsClassifier(n_neighbors=1)
        print("model intialization")
        self.knn.fit(self.X_train, self.y_train)
        print("model fitting")

    # Imagine that we obtained a new iris
    def predict(self, sl, sw, pl, pw):
        print("in predict function")
        self.X_new = np.array([[sl, sw, pl, pw]])
        print("New data: ", self.X_new)
        print(self.X_new.shape)
        print("data received into predict function")
        self.prediction = self.knn.predict(self.X_new)
        print("prediction done")
        print("Predicted flower name: ", self.iris['target_names'][self.prediction[0]])
        print("Accuracy of prediction: ", self.knn.score(self.X_test, self.y_test))
        # print(self.prediction)
        return [(self.iris['target_names'][self.prediction]), (self.knn.score(self.X_test, self.y_test))]
