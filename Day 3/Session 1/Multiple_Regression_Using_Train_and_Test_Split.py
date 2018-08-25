import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import sklearn
# Importing the dataset
marketing = pd.read_csv("C:\\Users\\app\\Desktop\\marketing.csv")

# Getting first five rows of the marketing dataset
marketing.head()

# Getting type marketing dataset
type(marketing)

# Getting columns in marketing dataset
marketing.columns

# Getting value of correlation between all columns
marketing.corr()

# Setting the features and target variables
X = marketing.as_matrix(['youtube', 'facebook'])
Y = marketing.sales


from sklearn.linear_model import LinearRegression

lm = LinearRegression()

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 5)

# Fitting the model
lm.fit(X_train, Y_train)

# Slope
print(lm.coef_)

# X intercept
print(lm.intercept_)

# Variance score i.e. how much variation is captured by the model
print(lm.score(X, Y))


Y_pred = lm.predict(X_test)

from sklearn.metrics import mean_squared_error

mse = np.mean((Y_test-Y_pred)**2)
mse = mean_squared_error(Y_test, Y_pred)

# Visualizing the Y and Y_pred
plt.title("Comparison of Y values and the Prediced values")
plt.xlabel("Testing Set")
plt.ylabel("Predicted values")
plt.scatter(Y_pred, Y_test, color = "black")


plt.scatter(X, Y)
min_X = min(X)
max_X = max(X)

m = lm.coef_[0]
b = lm.intercept_
plt.plot([min_X, max_X], [b, m*max_X + b], 'r')
plt.title("Fitted Regression Line")
plt.xlabel("X")
plt.ylabel("Y")






