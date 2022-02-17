import pandas as pd
dt5 = pd.read_csv("iris_data.csv")
dt5[1:5]
len(dt5)
dt5.petalLength[1:5]

X = [[0,0],[1,0],[1,1],[2,1],[2,1],[2,0]]
Y = [0,0,0,0,1,1,0]