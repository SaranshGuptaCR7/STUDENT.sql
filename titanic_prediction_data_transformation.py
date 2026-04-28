import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv('Titanic_Dataset.csv')
print(df.head(10))
sns.set_style('whitegrid')
sns.countplot(x='Survived', data=df)
plt.show()
sns.countplot(x='Gender', data=df, hue='Survived')
plt.show()
sns.countplot(x='Survived', data=df, palette='winter')
plt.show()
sns.countplot(x='Gender', data=df, hue='Gender', palette='winter')
plt.show()
sns.countplot(x='Embarked', data=df)
plt.show()
sns.countplot(x='Embarked', data=df)
plt.xticks(rotation=30, fontsize=28)
plt.show()