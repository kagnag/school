import pandas as pd

dt = pd.read_csv("buoi2_2.csv", delimiter=",")
dt

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dt.iloc[:,1:4], dt.nhan, test_size = 1, random_state = 100)

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion="gini", random_state = 100, max_depth = 5, min_samples_leaf = 3)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

clf.predict([[135,39,1]])

from sklearn.metrics import accuracy_score
print("Accuracy is ", accuracy_score(y_test, y_pred)*100)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred, labels = y_test)
