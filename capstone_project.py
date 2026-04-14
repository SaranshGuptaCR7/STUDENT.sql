import matplotlib.pyplot as plt
import pandas as pd
import warnings
import seaborn as sns
import numpy as np
warnings.filterwarnings('ignore')
df = pd.read_csv('heart.csv')
df.head()
df.shape
df.columns
df.describe()
df.isnull().sum()
print(df.info())
df.hist(figsize=(12, 12), layout=(5, 3))
df.plot(kind='box', subplots=True, layout=(5, 3), figsize=(12, 12))
plt.show()
sns.barplot(data=df, x='sex', y='chol', hue='target', palette='spring')
df['sex'].value_counts()
df['target'].value_counts()
df['thal'].value_counts()
plt.figure(figsize=(20, 10))
sns.heatmap(df.corr(), annot=True, cmap='terrain')
sns.countplot(data=df, x='sex', hue='target', palette='husl')
sns.countplot(x='target', data=df, palette='BuGn')
sns.countplot(x='ca', data=df, hue='target')
plt.show()