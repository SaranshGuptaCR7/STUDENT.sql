import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = pd.read_csv('Titanic_Dataset.csv')
print(df.head(20))
print(df.isnull().any())
print(df.isnull().sum())
sns.countplot(x='Gender', hue='Survived', data=df)
plt.show()
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.show()
sns.histplot(x='Age', kde=True, bins=40, data=df)
plt.show()
sns.countplot(x='Fare', data=df)
plt.show()
sns.countplot(x='Survived', hue='SibSp', palette='mako', data=df)
plt.show()
sns.countplot(x='Survived', hue='Parch', palette='mako', data=df)
plt.show()
sns.boxplot(x='Pclass', y='Age', data=df, palette='winter', hue='Survived')
plt.show()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.show()