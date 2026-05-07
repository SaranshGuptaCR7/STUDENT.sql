import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statisctics as std
df = pd.read_csv('Bestsellers_with_categories.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().any())
print(df.isnull().sum())
mode_genre = std.mode(df['Genre'])
genre_counts = df['Genre'].value_counts()
sns.barplot(x=genre_counts.index, y=genre_counts.values, color='lightcoral')
plt.title('Bar Chart of Genre Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45)
plt.show()
numeric_values = df[['User Rating', 'Price', 'Year', 'Reviews']]
sns.boxplot(data=numeric_values, palette='Set2')
plt.title('Box Plot of Numeric Variables', fontsize=14, fontweight='bold')
plt.xlabel('Variables', fontsize=12)
plt.ylabel('Values', fontsize=12)
plt.xticks(rotation=45)
plt.show()
df.groupby('Genre').size().plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('Set3'))