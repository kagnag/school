import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np

dt = pd.read_csv("Housing_2019.csv", index_col=0)
X = dt.iloc[:,[1,2,4,10]]
Y = dt.price

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=1.0/3, random_state=100)
len(X_train)

from sklearn import linear_model
lm = linear_model.LinearRegression()
lm.fit(X_train, y_train)
y_pred_lm = lm.predict(X_test)
err_lm = mean_squared_error(y_test, y_pred_lm)
err_lm
# 357828416.89302063 
np.sqrt(err_lm)
# 18916.353160506933
