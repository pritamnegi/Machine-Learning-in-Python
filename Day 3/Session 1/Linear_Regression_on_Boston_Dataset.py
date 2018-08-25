import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import sklearn

from sklearn.datasets import load_boston

boston = load_boston()

print(boston.keys())

print(boston.data.shape)

print(boston.feature_names)

print(boston.DESCR)

bos = pd.DataFrame(boston.data)

bos.columns = boston.feature_names

bos.corr()

X = bos.as_matrix(['RM', 'PTRATIO', 'LSTAT'])
Y = boston.target

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

lm = LinearRegression()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 5)


# Fitting the model
lm.fit(X_train, Y_train)


Y_pred = lm.predict(X_test)

from sklearn.metrics import mean_squared_error

mse = np.mean((Y_test-Y_pred)**2)
mse = mean_squared_error(Y_test, Y_pred)


