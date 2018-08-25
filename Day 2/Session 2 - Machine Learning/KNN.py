# KNN Algorithm

import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


iris = load_iris()

print(iris['feature_names'])

print(iris['target'])

X = iris.data

y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)


# Training the model using the KNN Algorithm

neigh = KNeighborsClassifier(n_neighbors=3)
fit = neigh.fit(X_train, y_train)
predict = neigh.predict(X_test)
acc = sklearn.metrics.accuracy_score(y_test, predict)
print("Accuracy of KNN with K = 3 is: ", acc)
