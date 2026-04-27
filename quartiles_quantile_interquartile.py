import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Bestsellers_with_categories.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().any())
print(df.isnull().sum())
quartile_price_1 = np.quantile(df['Price'], 0.25)
print("First Quartile (Q1) of Price:", quartile_price_1)
quartile_price_2 = np.quantile(df['Price'], 0.50)
print("Second Quartile (Q2) of Price:", quartile_price_2)
quartile_price_3 = np.quantile(df['Price'], 0.75)
print("Third Quartile (Q3) of Price:", quartile_price_3)
IDBM = quartile_price_3 - quartile_price_1
print("Interquartile Range (IQR) of Price:", IDBM)
quartile_user_1 = np.quantile(df['User Rating'], 0.25)
print("First Quartile (Q1) of User Rating:", quartile_user_1)
quartile_user_2 = np.quantile(df['User Rating'], 0.50)
print("Second Quartile (Q2) of User Rating:", quartile_user_2)
quartile_user_3 = np.quantile(df['User Rating'], 0.75)
print("Third Quartile (Q3) of User Rating:", quartile_user_3)
IDBM_user = quartile_user_3 - quartile_user_1
print("Interquartile Range (IQR) of User Rating:", IDBM_user)
sns.boxplot(x=df['Price'], y=df['User Rating'], color='lightcoral')
plt.title('Box Plot of Price vs User Rating', fontsize=16, fontfamily='italic', color='darkred')
plt.xlabel('Price', fontsize=12, fontfamily='monospace', color='darkred')
plt.ylabel('User Rating', fontsize=12, fontfamily='helvetica', color='violet')
plt.legend()
plt.show()