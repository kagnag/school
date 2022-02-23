# 1
import numpy as np
import pandas as pd
dt = pd.read_csv("winequality-white.csv", delimiter=";")
dt[0:10]

len(dt)
# tap du lieu co 4898 phan tu

np.unique(dt.quality)
dt.quality.value_counts()
dt.iloc[1:5,0:11]
# 7 gia tri nhan khac nhau

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dt.iloc[:,0:11], dt.quality, test_size = 2/10.0, random_state = 100)
X_train[1:5]
X_test[1:5]
y_train[1:5]
y_test[1:5]
len(y_test)
np.unique(y_test)
y_test.value_counts()
# co 980 phan tu trong tap test
# so luong phan tu trong tap test
# 6    452
# 5    280
# 7    178
# 8     36
# 4     26
# 3      6
# 9      2

from sklearn.tree import DecisionTreeClassifier
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 10, max_depth = 7, min_samples_leaf = 5)
clf_entropy.fit(X_train, y_train)
clf_entropy
y_pred = clf_entropy.predict(X_test)

from sklearn.metrics import accuracy_score
print("Accuracy is ", accuracy_score(y_test, y_pred)*100)

mm = np.unique(y_test)
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred, labels = mm)

y_pred6 = clf_entropy.predict(X_test[1:7])
print("Accuracy is ", accuracy_score(y_pred6, y_pred6)*100)
confusion_matrix(y_pred6, y_pred6, labels = mm)







