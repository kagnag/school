# su dung tap du lieu co san "iris"
from sklearn.datasets import load_iris
iris_dt =load_iris()
iris_dt.data[1:5]
iris_dt.target[1:5]

# phan chia tap du lieu de xay dung mo hinh va kiem tra theo nghi thuc Hold-out
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_dt.data, iris_dt.target, test_size = 1/3.0, random_state = 5)

X_train[1:6]
X_train[1:6,1:3]
y_train[1:6]
X_test[6:10]
y_test[6:10]

# xay dung mo hinh K lang gieng KNN, voi 5 lang gieng
from sklearn.neighbors import KNeighborsClassifier
Mohinh_KNN = KNeighborsClassifier(n_neighbors = 5)
Mohinh_KNN.fit(X_train, y_train)

# du doan nhan cho cac phan tu trong tap kiem tra
# du doan
y_pred = Mohinh_KNN.predict(X_test)
y_test
Mohinh_KNN.predict([[4, 4, 3, 3]])

# tinh do chinh xac cho gia tri du doan cua phan tu trong tap kiem tra
from sklearn.metrics import accuracy_score
print ("Accuracy is", accuracy_score(y_test, y_pred)*100)
 
# tinh do chinh xac cho gia tri du doan thong qua ma tran con
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred, labels = [2, 0, 1])


