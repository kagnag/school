from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB

import pandas as pd
dulieu = pd.read_csv("iris_data.csv")
X = dulieu.iloc[:,0:4]
y = dulieu.nhan

# Phan chia du lieu thanh tap test va train
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
# xay dung mo hinh dua tren phan phoi xac xuat tuan theo Gausian
model = GaussianNB()
model.fit(X_train, y_train)
print(model)
# du doan
thucte = y_test
dubao = model.predict(X_test)
thucte
dubao

from sklearn.metrics import confusion_matrix
cnf_matrix_gnb = confusion_matrix(thucte, dubao)
print(cnf_matrix_gnb)

from sklearn.model_selection import KFold
kf = KFold(n_splits = 15) # chia tap du lieu thanh 15 phan

# neu du lieu doc tu dataset cua sklearn
for train_index, test_index in kf.split(X):
	print("Train", train_index, "Test:", test_index) # in gia tri chi so cua tap huan luyen va tap kiem train
	X_train, X_test = X[train_index], X[test_index] # tao bien X_train va X_test de luu tru thuoc tinh cua tap
	y_train, y_test = y[train_index], y[test_index] # tao bien y_train va y_test de luu tru nhan cua tap
	print ("X_test", X_test)
	print ("======================")
	
# neu du lieu doc tu file boi thu vien pandas
for train_index, test_index in kf.split(X):
	print("Train", train_index, "Test:", test_index)
	X_train, X_test = X.iloc[train_index,], X.iloc[test_index,]
	y_train, y_test = y.iloc[train_index], y.iloc[test_index] 
	print ("X_test", X_test)
	print ("======================")
	
