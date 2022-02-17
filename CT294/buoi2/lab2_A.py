# lay file iris truc tiep tu sklearn
from sklearn.datasets import load_iris
iris_dt = load_iris()
iris_dt.data[1:5] # thuoc tinh cua tap iris
iris_dt.target[1:5] # gia tri cua nhan /class

# phan chia tap du lieu de xay dung mo hinh va kiem tra theo nghi thuc Hold-out
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_dt.data, iris_dt.target, test_size = 1/3.0, random_state = 5)
X_train[1:6]
X_train[1:6, 1:3]
y_train[1:6]
X_test[6:10]
y_test[6:10]

# xay dung mo hinh cay quyet dinh dua tren chi so Gini voi do sau cua cay bang 3, nut nhanh it nhat co 5 phan tu
from sklearn.tree import DecisionTreeClassifier
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth = 3, min_samples_leaf = 5)
clf_gini.fit(X_train, y_train)

# du doan nhan co cac phan tu trong tap kiem tra
y_pred = clf_gini.predict(X_test)
y_test
clf_gini.predict([[4, 4, 3 ,3]])

# tinh do chinh xac
from sklearn.metrics import accuracy_score
print("Accuracy is ", accuracy_score(y_test, y_pred)*100)

# tinh do chinh xac cho gia tri du doan thong qua ma tran con
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred, labels = [2,0,1])
