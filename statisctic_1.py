import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv('Titanic_Dataset.csv')
print(df.head(10))
print(df.tail(10))
print(df.columns)
sns.countplot(x='Gender', hue='Survived', palette='Set2', data=df)
plt.show()
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm')
plt.show()
print(df.isnull().sum())
print(df.isnull().any())
print(df.dtypes)