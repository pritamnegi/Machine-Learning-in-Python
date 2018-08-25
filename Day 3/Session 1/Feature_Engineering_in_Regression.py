import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import sklearn


insurance = pd.read_csv("C:\\Users\\app\\Desktop\\insurance.csv")

insurance.columns

insurance.head()

insurance.corr()

import statsmodels.formula.api as smf
reg = smf.ols(formula = "expenses ~ age + bmi + children", data = insurance).fit()
reg.summary()


dummies = pd.get_dummies(insurance['smoker'], drop_first = True)
dummies = dummies.rename(columns = lambda x: 'smoker_' + str(x))
dummies

df = pd.concat([insurance, dummies], axis = 1)

df = df.drop('smoker', axis = 1)


reg = smf.ols(formula = "expenses ~ age + bmi + smoker_yes", data = df).fit()
reg.summary()

