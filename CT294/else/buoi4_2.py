import numpy as np
import pandas as pd

dt = pd.read_csv("winequality-red.csv", delimiter=";")
dt.head(5)
len(dt)
# 1599

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dt.iloc[:,0:11], dt.quality, test_size=1.0/5, random_state=100)

from sklearn.ensemble import RandomForestClassifier
RForest = RandomForestClassifier(n_estimators=100, min_samples_split=10, max_depth=10)
RForest.fit(X_train, y_train)
y_pred_RForest = RForest.predict(X_test)

from sklearn.metrics import accuracy_score
print("Accuracy is ", accuracy_score(y_test, y_pred_RForest)*100)
# 69.6875
mn = np.unique(y_test)
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred_RForest, labels=mn)

