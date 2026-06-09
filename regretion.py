import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
diabetes_x, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_x = diabetes_x[:, np.newaxis, 2] 
diabetes_x_train = diabetes_x[:-20]
diabetes_x_test = diabetes_x[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
regr = linear_model.LinearRegression()
regr.fit(diabetes_x_train, diabetes_y_train)
diabetes_y_pred = regr.predict(diabetes_x_test)
print("Coefficients: \n", regr.coef_)
print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
print("Coefficients of determination: 1 is perfect prediction rest is something that u have to predict %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))
plt.scatter(diabetes_x_test, diabetes_y_test, color="black")
plt.plot(diabetes_x_test, diabetes_y_pred, color="blue", linewidth=3)
plt.show()