import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
df = pd.read_csv('Titanic_Dataset.csv')
print(df.head(10))
print(df.tail(10))
print(df.columns)
print(df.isnull().sum())
print(df.isnull().any())
print(df.dtypes)
mean_age = np.mean(df['Age'])
print("Mean Age:", mean_age)
mean_fare = np.mean(df['Fare'])
print("Mean Fare:", mean_fare)