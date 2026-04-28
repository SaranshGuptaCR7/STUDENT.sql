import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv("Titanic_Dataset.csv")
print(df.head(5))
print(df.dtypes)
nominal_cat = ['Name', 'Ticket', 'Cabin']
ordinal_cat = ['Gender', 'Embarked']
df['Gender'].value_counts()
gender_categories = ['Male', 'Female']
df['Gender'] = pd.Categorical(df['Gender'], gender_categories, ordered=True)
median_index = np.median(df['Gender'].cat.codes)
median_gender = gender_categories[int(median_index)]
print(median_gender)
df['Embarked'].value_counts()
embarked_categories = ['S', 'C', 'Q']
df['Embarked'] = pd.Categorical(df['Embarked'], embarked_categories, ordered=True)
median_index_embarked = np.median(df['Embarked'].cat.codes)
median_embarked = embarked_categories[int(median_index_embarked)]
print(median_embarked)