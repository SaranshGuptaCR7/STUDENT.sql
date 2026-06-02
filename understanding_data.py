import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
df = pd.read_csv("titanic.csv", sep="\t")
print(df.head())
df.shape
print(df.isnull().sum())
print(df.isnull().any())
sns.heatmap(df.isnull(), cmap="spring", annot=True)
plt.show()
print(df.head())
df.dropna(inplace=True)
sns.heatmap(df.isnull(), cbar=False, annot=True)
plt.show()
print(df.isnull().sum())
print(pd.get_dummies(df["Sex"]).head())
sex = pd.get_dummies(df["Sex"], drop_first=True)
sex.head(9)
print(pd.get_dummies(df["Embarked"]).head(9))
embarked = pd.get_dummies(df["Embarked"], drop_first=True)
pclass = pd.get_dummies(df["Pclass"], drop_first=True)
pclass.head(9)
Titanic = pd.concat([df, sex, pclass, embarked], axis=1)
print(Titanic.head())