import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv("titanic.csv")
print(df.head(5))
print(df.dtypes)
print(df.isnull().sum())
print(df.isnull().any())
df['Sex'].value_counts()
gender_categories = ['Male', 'Female']
df['Gender'] = pd.Categorical(df['Sex'], gender_categories, ordered=True)
median_index = np.median(df['Gender'].cat.codes)
median_gender = gender_categories[int(median_index)]
print(median_gender)
df['Survived'].value_counts()
survived_categories = ['Not Survived', 'Survived']
df['Survival_Status'] = pd.Categorical(df['Survived'], survived_categories, ordered=True)
median_index = np.median(df['Survival_Status'].cat.codes)
median_survival_status = survived_categories[int(median_index)]
print(median_survival_status)
df['Pclass'].value_counts()
pclass_categories = ['Class 3', 'Class 2', 'Class 1']
df['Class'] = pd.Categorical(df['Pclass'], pclass_categories, ordered=True)
median_index = np.median(df['Class'].cat.codes)
median_class = pclass_categories[int(median_index)]
print(median_class)
df['Survival_Status'].value_counts().plot(kind='bar')
plt.title('Survival Status Distribution')
plt.xlabel('Survival Status')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
pd.crosstab(df['Sex'], df['Survival_Status']).plot(kind='bar')
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
pd.crosstab(df['Class'], df['Survival_Status']).plot(kind='bar')
plt.title("Survival by Class")
plt.xlabel("Class")
plt.ylabel("Count")
plt.show()