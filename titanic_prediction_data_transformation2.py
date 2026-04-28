import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv('Titanic_Dataset.csv')
print(df.head(10))
num_data = df.drop(['Name', 'Ticket', 'Cabin', 'Embarked', 'Gender'],axis=1)
labels = ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
for label in labels:
    plt.boxplot(num_data[label])
    print("Distribution of", label)
    plt.show()
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
num_data = scaler.fit_transform(num_data)    