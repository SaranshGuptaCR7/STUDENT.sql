import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
df = pd.read_csv('Bestsellers_with_categories.csv')
print(df.head())   
print(df.isnull().sum())    
null = df.isnull().sum()
plt.plot(null, marker='o', color='magenta')
plt.show()
sns.pairplot(df[['Price', 'Year']])
plt.xlabel('Price')
plt.ylabel('Year')
plt.show()
sns.boxplot(df[['Price', 'Year']], color='lightblue')
plt.show()