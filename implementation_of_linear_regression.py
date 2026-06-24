import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("xydataset(1).csv", header=None)
df = df.drop(columns=[0])
x_train = df.iloc[:,0].values
y_train = df.iloc[:,1].values
m = 0
b = 0
step_size = 0.0001
steps = 1000
n = len(x_train)
for i in range(steps):
    y_pred = m * x_train + b
    dm = (-2/n) * np.sum(x_train * (y_train - y_pred))
    db = (-2/n) * np.sum(y_train - y_pred)
    m = m - step_size * dm
    b = b - step_size * db
y_pred = m * x_train + b
print("Slope (m):", m)
print("Intercept (b):", b)
mse = np.mean((y_train - y_pred)**2)
print("Mean Squared Error:", mse)
ss_total = np.sum((y_train - np.mean(y_train))**2)
ss_residual = np.sum((y_train - y_pred)**2)
r2 = 1 - (ss_residual / ss_total)
print("R² Score:", r2)
plt.scatter(x_train, y_train, color="blue", label="Actual Data")
plt.plot(x_train, y_pred, color="red", label="Regression Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression using Gradient Descent")
plt.legend()
plt.show()