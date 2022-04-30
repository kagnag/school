import imp
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
# import ma hoa
from sklearn.preprocessing import LabelEncoder 
le = LabelEncoder()
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()


dt = pd.read_csv("D:\Car_Insurance_Claim.csv", delimiter=",")

def mahoa():
    print("Du lieu truoc khi ma hoa\n{}",dt.iloc[:20,:])

    dt['ID'] = le.fit_transform(dt['ID'])
    dt['AGE'] = le.fit_transform(dt['AGE'])
    dt['GENDER'] = le.fit_transform(dt['GENDER'])
    dt['RACE'] = le.fit_transform(dt['RACE'])
    dt['DRIVING_EXPERIENCE'] = le.fit_transform(dt['DRIVING_EXPERIENCE'])
    dt['EDUCATION'] = le.fit_transform(dt['EDUCATION'])
    dt['INCOME'] = le.fit_transform(dt['INCOME'])
    dt['CREDIT_SCORE'] = le.fit_transform(dt['CREDIT_SCORE'])
    dt['VEHICLE_OWNERSHIP'] = le.fit_transform(dt['VEHICLE_OWNERSHIP'])
    dt['VEHICLE_YEAR'] = le.fit_transform(dt['VEHICLE_YEAR'])
    dt['MARRIED'] = le.fit_transform(dt['MARRIED'])
    dt['CHILDREN'] = le.fit_transform(dt['CHILDREN'])
    dt['POSTAL_CODE'] = le.fit_transform(dt['POSTAL_CODE'])
    dt['ANNUAL_MILEAGE'] = le.fit_transform(dt['ANNUAL_MILEAGE'])
    dt['VEHICLE_TYPE'] = le.fit_transform(dt['VEHICLE_TYPE'])
    # dt['SPEEDING_VIOLATIONS'] = le.fit_transform(dt['SPEEDING_VIOLATIONS'])
    # dt['DUIS'] = le.fit_transform(dt['DUIS'])
    # dt['PAST_ACCIDENTS'] = le.fit_transform(dt['PAST_ACCIDENTS'])
    dt['OUTCOME'] = le.fit_transform(dt['OUTCOME'])

    print("Du lieu sau khi ma hoa\n{}",dt.iloc[:20,:])
# mahoa()


# Cay quyet dinh voi tat ca du lieu
def cqd_all_data():
    mahoa()
    print("Giai thuat cay quyet dinh")
    avg = 0
    for i in range(10):
        X_train, X_test, y_train, y_test = train_test_split(dt, dt.OUTCOME, test_size = 2/5, random_state = 100*i)
        clf = DecisionTreeClassifier(criterion="gini", random_state = 500, max_depth = 3, min_samples_leaf = 1)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        print("Lan lap {}: Accuracy is {}".format(i+1,round(accuracy_score(y_test, y_pred)*100, 3)))
        
        avg += accuracy_score(y_test, y_pred)*100

    # print("Do chinh xac trung binh la:", avg/10)
    # print(confusion_matrix(y_test, y_pred, labels = y_test))
# cqd_all_data()


# Tim max_depth, min_sample_leaf
def find_min_max():
    print("Tim max_depth, min_sample_leaf")
    max = -1
    m_depth = 0
    m_s_leaf = 0

    X_train, X_test, y_train, y_test = train_test_split(dt.iloc[:,15:18], dt.OUTCOME, test_size = 2/5, random_state = 100)
    for i in range(1,11):
        for j in range(1,11):
            clf = DecisionTreeClassifier(criterion="gini", random_state = 100, max_depth = i, min_samples_leaf = j)
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)
            # clf.predict([[1,1,1]])
            print("Voi i = {}, j = {}, Accuracy is {}".format(i,j,round(accuracy_score(y_test, y_pred)*100, 3)))

            if max < round(accuracy_score(y_test, y_pred)*100, 3):
                max = round(accuracy_score(y_test, y_pred)*100, 3)
                m_depth = i
                m_s_leaf = j
        print("\n")
    print("Voi max_depth = {}, min_sample_leaf = {}, Accuracy = {} cho ra do chinh xac cao nhat".format(m_depth, m_s_leaf, max))        
# find_min_max()


# cay quyet dinh
def cqd():
    print("Giai thuat cay quyet dinh")
    avg = 0
    for i in range(10):
        X_train, X_test, y_train, y_test = train_test_split(dt.iloc[:,2:5], dt.OUTCOME, test_size = 2/5, random_state = 100*i)
        clf = DecisionTreeClassifier(criterion="gini", random_state = 500, max_depth = 5, min_samples_leaf = 2)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        # clf.predict([[1,1,1]])
        print("Lan lap {}: Accuracy is {}".format(i+1,round(accuracy_score(y_test, y_pred)*100, 3)))
        
        avg += accuracy_score(y_test, y_pred)*100

    # print("Do chinh xac trung binh la:", avg/10)
    # print(confusion_matrix(y_test, y_pred, labels = y_test))
# cqd()


# Bayes
def bayes():
    print("Giai thuat Bayes")
    for i in range(10):
        X_train, X_test, y_train, y_test = train_test_split(dt.iloc[:,15:18], dt.OUTCOME, test_size = 2/5, random_state = 100*i)
        model = GaussianNB()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print ("Lan lap {} Accuracy is {}".format(i+1,round(accuracy_score(y_test, y_pred)*100, 3)))
    # print(confusion_matrix(y_test, y_pred))
# bayes()


# Tim n_neighbors tot nhat
def find_n_neighbors():
    max = -1
    j = 0
    for i in range(1,21):
        X_train, X_test, y_train, y_test = train_test_split(dt.iloc[:,15:18], dt.OUTCOME, test_size = 2/5, random_state = 100)
        Mohinh_KNN = KNeighborsClassifier(n_neighbors = i)
        Mohinh_KNN.fit(X_train, y_train)
        y_pred = Mohinh_KNN.predict(X_test)
        print("Voi n_neighbors = {}, Accuracy is {}".format(i,round(accuracy_score(y_test, y_pred)*100, 3)))
        if max < round(accuracy_score(y_test, y_pred)*100, 3):
                max = round(accuracy_score(y_test, y_pred)*100, 3)
                j = i
    print("\nVoi n_neighbors = {}, Accuracy = {} cho ra do chinh xac cao nhat".format(j, max))
# find_n_neighbors()


# KNN
def knn():
    print("Giai thuat KNN")
    for i in range(10):
        X_train, X_test, y_train, y_test = train_test_split(dt.iloc[:,15:18], dt.OUTCOME, test_size = 2/5, random_state = 100*i)
        Mohinh_KNN = KNeighborsClassifier(n_neighbors = 6)
        Mohinh_KNN.fit(X_train, y_train)
        y_pred = Mohinh_KNN.predict(X_test)
        # Mohinh_KNN.predict([[1,1,1]])
        print("Lan lap {} Accuracy is {}".format(i+1,round(accuracy_score(y_test, y_pred)*100, 3)))
    # print(confusion_matrix(y_test, y_pred, labels = [1, 0, 1]))
# knn()