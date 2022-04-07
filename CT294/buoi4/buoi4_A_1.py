import numpy as np
import matplotlib.pyplot as plt

X = np.array([1,2,4])
Y = np.array([2,3,6])

plt.axis([0,5,0,8])
plt.plot(X,Y,"ro",color="blue")
plt.xlabel("Gia tri thuoc tinh X")
plt.ylabel("Gia tri du doan Y")
plt.show()

def LR1(X, Y, eta, lanlap, theta0, theta1):
    m = len(X) # so luong phan tu
    for k in range(0, lanlap):
        print("Lan lap: ", k)
        for i in range(0, m):
            h_i = theta0 + theta1*X[i]
            # theta0
            theta0 = theta0 + eta*(Y[i] - h_i)*1
            print("Phan tu", i, "y =", Y[i], "h =", h_i, "gia tri theta0", round(theta0, 3))
            # theta1
            theta1 = theta1 + eta*(Y[i] - h_i)*X[i]
            print("Phan tu", i, "gia tri theta1 = ", round(theta1, 3))
    return [round(theta0, 3), round(theta1, 3)]

theta = LR1(X, Y, 0.2, 1, 0, 1) # theta 1 buoc
X1 = np.array([1, 6])
Y1 = theta[0] + theta[1]*X1

theta2 = LR1(X, Y, 0.2, 2, 0, 1) # theta 2 buoc lap
X2 = np.array([1, 6])
Y2 = theta2[0] + theta2[1]*X2

plt.axis([0, 7, 0, 10])
plt.plot(X, Y, "ro", color="blue")

plt.plot(X1, Y1, color="violet") # duong hoi quy lan lap 1
plt.plot(X2, Y2, color="green") # duong hoi quy lan lap 2

plt.xlabel("Gia tri thuoc tinh X")
plt.ylabel("Gia tru du doan Y")
plt.show()

# thay doi toc do hoc bang 0.1
theta3 = LR1(X, Y, 0.1, 1, 0, 1) # theta 1 buoc
X3 = np.array([1, 6])
Y3 = theta3[0] + theta3[1]*X3

theta4 = LR1(X, Y, 0.1, 2, 0, 1) # theta 2 buoc lap
X4 = np.array([1, 6])
Y4 = theta4[0] + theta4[1]*X4
plt.axis([0, 7, 0, 10])
plt.plot(X, Y, "ro", color="blue")

plt.plot(X3, Y3, color="pink") # duong hoi quy lan lap 1
plt.plot(X4, Y4, color="green") # duong hoi quy lan lap 2

plt.xlabel("Gia tri thuoc tinh X")
plt.ylabel("Gia tru du doan Y")
plt.show()

theta = LR1(X, Y, 0.2, 2, 0, 1)
y1 = theta[0] + theta[1]*0
y2 = theta[0] + theta[1]*3
y3 = theta[0] + theta[1]*5

 # hoac vong lap
# XX = [0, 3, 5]
# for i in range(0, 3):
#     YY = theta[0] + theta[1]*XX[i]
#     print(round(YY, 3))