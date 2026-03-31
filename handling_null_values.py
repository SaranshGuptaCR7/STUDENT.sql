import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv('penguins_data.csv')
print(df.head(10))
print(df.isnull().sum())
df = df.dropna(how='all')        
df.fillna('1', inplace=True)
df.fillna(method='ffill', inplace=True)
print(df.isnull().sum(), inplace=True)
df.fillna(method='ffill', inplace=True)
df.interpolate()