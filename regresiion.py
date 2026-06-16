import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('xydataset.csv')
X = df.iloc[:,1].values
Y = df.iloc[:,2].values
n = len(X)
mean_x = np.mean(X)
mean_y = np.mean(Y)
b = np.sum((X - mean_x)*(Y - mean_y)) / np.sum((X - mean_x)**2)
a = mean_y - b*mean_x
print("Intercept (a) =", a)
print("Slope (b) =", b)
print("Regression Equation:")
print("Y =", a, "+", b, "* X")
Y_pred = a + b*X
plt.scatter(X, Y, color='blue', label='Data Points')
plt.plot(X, Y_pred, color='red', label='Regression Line')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")
plt.legend()
plt.show()