import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Titanic_Dataset.csv')
print(df.head())
minimum_age  = df['Age'].min()
print("Minimum age:", minimum_age)
maximum_age  = df['Age'].max()
print("Maximum age:", maximum_age)
bins = [0, 15, 30, 45, 60, 75]
df['binned_age'] = pd.cut(df['Age'], bins)
print(df['binned_age'].head())
age_labels = ["Young", "Young-Adult", "Middle Aged","Middle-Older Age","Senior"]
df['binned_age'] = pd.cut(df['Age'], bins, labels= 'age_labels')
df['binned_age'].value_count().plot(kind='bar')
plt.title('Dance classes & Age distributiuon')
plt.xlabel('Ages')
plt.ylabel('Count')
labels = ["PassengerId", "Survived","Pclass","SipSp","Parch","Fare"]
for label in labels:
   print("Distribution of:", label)
   sns.histplot(df[label]) 
   plt.show()
   print("Skewness-", df[label].skew())
df['log_SipSp'] = np.log(df['SipSp']) 
df['log_Parch'] = np.log(df['Parch'])  
df['log_Fare'] = np.log(df['Fare'])   