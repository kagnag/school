import imp
import pandas as pd
dulieu = pd.read_csv("winequality-red.csv", delimiter=";")
dulieu
dulieu.quality
len(dulieu)
# a) tap du lieu co 1599 phan tu

import numpy as np
np.unique(dulieu.quality)
dulieu.quality.value_counts()
# b) co  6 gia tri nhan khac nhau

# c)
from sklearn.model_selection import KFold
kf = KFold(n_splits = 50, shuffle = True, random_state = 3000)
X = dulieu.iloc[:,0:11]
y = dulieu.iloc[:,11]

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
Mohinh_KNN = KNeighborsClassifier(n_neighbors = 9)
model_BN = GaussianNB()
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

for train_index, test_index in kf.split(X):
	print("Train", train_index, "Test:", test_index)
	X_train, X_test = X.iloc[train_index,], X.iloc[test_index,]
	y_train, y_test = y.iloc[train_index], y.iloc[test_index] 
	print ("X_test", X_test)
	len(train_index)
	# 1586
	len(test_index)	
	# 31
	
	# d)
	Mohinh_KNN.fit(X_train, y_train)
	y_pred_knn = Mohinh_KNN.predict(X_test)
	
	# i)
	print ("Accuracy KNN is", accuracy_score(y_test, y_pred_knn)*100)

	mm = np.unique(y_test)
	confusion_matrix(y_test, y_pred_knn, labels = mm)

	# e)
	model_BN.fit(X_train, y_train)
	dubao = model_BN.predict(X_test)
	print ("Accuracy Bayes is", accuracy_score(y_test, dubao)*100)
	
	mm = np.unique(y_test)
	print(mm)
	confusion_matrix(y_test, dubao, labels = mm)
	
# ii)	
t7 = y_test[0:7]
p7 = y_pred_knn[0:7]
print("7 Accuracy KNN is ", accuracy_score(t7, p7)*100)

# f)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dulieu.iloc[:,0:11], dulieu.quality, test_size = 1/3.0, random_state = 5)
len(X_test)
Mohinh_KNN.fit(X_train, y_train)
y_pred_knn = Mohinh_KNN.predict(X_test)

print ("Accuracy KNN is", accuracy_score(y_test, y_pred_knn)*100)

mm = np.unique(y_test)
confusion_matrix(y_test, y_pred_knn, labels = mm)

t7 = y_test[0:7]
p7 = y_pred_knn[0:7]
print("7 Accuracy KNN is ", accuracy_score(t7, p7)*100)

model_BN.fit(X_train, y_train)
dubao = model_BN.predict(X_test)
print ("Accuracy Bayes is", accuracy_score(y_test, dubao)*100)
mm = np.unique(y_test)
print(mm)
confusion_matrix(y_test, dubao, labels = mm)

