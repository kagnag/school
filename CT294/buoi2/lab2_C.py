# doc du lieu vao bien "dulieu"
import pandas as pd
dulieu = pd.read_csv("housing_RT.csv", index_col=0)
dulieu.iloc[1:5,]

# su dung nghi thuc hold-out Phan chia tap du lieu huan luyen
from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(iris_dt.data, iris_dt.target, test_size = 1/3.0, random_state = 100)
X_train, X_test, y_train, y_test = train_test_split(dulieu.iloc[:,1:5], dulieu.iloc[:,0], test_size = 1/3.0, random_state = 100)
X_train.iloc[1:5,]
X_test
y_test[1:5]

# xay dung mo hinh
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, y_train)

# du bao va danh gia mo hinh
# du doan gia tri nhan
y_pred = regressor.predict(X_test)
y_test[1:5]
y_pred[1:5]
# danh gia ket qua du doan gia tri nha thong qua chi so MSE va RMSE
from sklearn.metrics import mean_squared_error
err = mean_squared_error(y_test, y_pred)
err
import numpy as np
np.sqrt(err)