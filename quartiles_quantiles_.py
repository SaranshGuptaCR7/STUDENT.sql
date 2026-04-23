import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv('Titanic_Dataset.csv')
print(df.head(10))
print(df.describe())
print(df.info())
print(df.isnull().sum())
plt.box(df['Age'])
plt.title('Age distribution', fontfamily='cursive', fontweight='bold')
plt.show()
plt.box(df['Pclass'])  
plt.title('Passenger class distribution', fontfamily='cursive', fontweight='bold')
plt.show()