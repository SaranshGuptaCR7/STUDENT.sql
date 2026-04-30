import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
df = pd.read_csv('Titanic_Dataset.csv')
print(df.head())
sns.boxplot(data=df, x='Embarked', y='Age')
plt.show()
plt.scatter(x=df['Fare'], y=df['Survived'])
plt.ylabel('Survived')
plt.xlabel('Fare')
plt.show()
plt.scatter(x=df['Parch'], y=df['Survived'])
plt.ylabel('Survived')
plt.xlabel('Parched')
plt.show()
plt.scatter(x=df['SibSp'], y=df['Survived'])
plt.ylabel('Survived')
plt.xlabel('SibSp')
plt.show()
association_cateoragy = pd.crosstab(df['Gender'], df['Embarked'])
print(association_cateoragy)