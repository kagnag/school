import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np

dt = pd.read_csv("Housing_2019.csv", index_col=0)
X = dt.iloc[:,[1,2,4,10]]
Y = dt.price

import sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=1.0/3, random_state=100)
len(X_train)

from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor(random_state=0)

bagging_regtree = BaggingRegressor(base_estimator=tree, n_estimators=10, random_state=42)
bagging_regtree.fit(X_train, y_train)
y_pred = bagging_regtree.predict(X_test)
err = mean_squared_error(y_test, y_pred)
err
np.sqrt(err)