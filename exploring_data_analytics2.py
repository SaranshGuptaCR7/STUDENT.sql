import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = pd.read_csv('Iris_Dataset.csv')
print(df.head(10))
print(df.isnull().any())
print(df.isnull().sum())
labels = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
for label in labels:
    print("Distribution of label:", label)
    sns.boxplot(df[label])
    plt.show()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.show()
for label in labels:
    print("Distribution of label:", label)
    sns.histplot(df[label], kde=True, bins=40)
    plt.show()
for label in labels:
    print("Skweness of label:", label)
    print(df[label].skew())    