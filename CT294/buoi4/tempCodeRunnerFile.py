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