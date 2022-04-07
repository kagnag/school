import pandas as pd
import matplotlib.pyplot as plt

dt = pd.read_csv("Housing_2019.csv", index_col=0)
dt.iloc[2:4,]
X = dt.iloc[:,[1,2,3,4,10]]
X.iloc[1:5, ]
y = dt.price

plt.scatter(dt.lotsize, dt.price)
plt.show()

# huan luyen mo hinh 
import sklearn
from sklearn import linear_model
lm = linear_model.LinearRegression()
lm.fit(X[1:520], y[1:520])

print(round(lm.intercept_, 3))
print(lm.coef_)
# du bao gia nha cho 20 phan tu cuoi cung trong tap du lieu
y = dt.price
y_test = y[-20:]
X_test = X[-20:]
y_pred = lm.predict(X_test)
# so sanh gia tri thuc te va gia tri du bao
y_pred
y_test
# danh gia
from sklearn.metrics import mean_squared_error
import numpy as np
err = mean_squared_error(y_test, y_pred)
print(round(err, 3))
np.sqrt(err)

# Có bao nhiêu thuộc tính, đó là những thuộc tính nào đã được sử dụng để dự đoán giá nhà?
    # 11 thuoc tinh những thuộc tính dùng để dự đoán giá nhà lotsize  bedrooms  bathrms  stories  garagepl
# Xác định số lượng theta và các giá trị của nó. 
    # 6 gia tri theta
# Dữ liệu được sử dụng để huấn luyện mô hình?
    # lấy từ phần tủ thứ1 đến phần tử thư 519
# Dữ liệu được sử dụng để dự báo mô hình?
    # 20 phần tử cuối cùng của tập dữ liệu
# Độ chính xác được đánh giá bằng chỉ số gì và giá trị của nó?
    # msr = 288877136.084 và rmsr 16996.385971252897