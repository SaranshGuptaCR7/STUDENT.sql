import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
df = pd.read_csv('weather_dataset.csv')
print(df.head(10))
print(df.tail(10))
print(df.isnull().sum())
mean_temperature = np.mean(df['Temperature (C)'])
print("Mean Temperature:", mean_temperature)
median_temperature = np.median(df['Temperature (C)'])
print("Median Temperature:", median_temperature)
var_tempetature = np.var(df['Temperature (C)'])
print("Variance of Temperature:", var_tempetature)
standard_temperature = np.std(df['Temperature (C)'])
print("Standard Deviation of Temperature:", standard_temperature)
for i in range(1, 13):
    month = df.loc[df['month'] == i]['Temperature (C)']
    print("For month"+str(i))
    print("Mean Temperature:"+ str(np.mean(month)))
    print("Standard Deviation:"+ str(np.std(month)))