import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('petrol_consumption.csv')
print(df.head())
print(df.describe())
x = df[['Petrol_tax', 'Average_income', 'Paved_Highways', 'Population_Driver_licence(%)']]
y = df['Petrol_Consumption']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x_train, y_train)
coeff_df = pd.DataFrame(regression.coef_, x.columns, columns=['Coefficient'])
print(coeff_df)
y_pred = regression.predict(x_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)
from sklearn import metrics
print("Mean Absolute Error:", round(metrics.mean_absolute_error(y_test, y_pred), 26))
print("Mean Squared Error:", round(metrics.mean_squared_error(y_test, y_pred),11))
print("Root Mean Squared Error:", round(np.sqrt(metrics.mean_squared_error(y_test, y_pred)),9))