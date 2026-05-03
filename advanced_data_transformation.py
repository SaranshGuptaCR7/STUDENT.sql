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
bins_user_rating = np.arange(0, 5.5, 0.5)
df['binned_user_rating'] = pd.cut(df['User Rating'], bins=bins_user_rating)
skewness_user_rating = df['User Rating'].skew()
print("Skewness of User Rating:", skewness_user_rating)
skeness_price = df['Price'].skew()
print("Skewness of Price:", skeness_price)
skeness_year = df['Year'].skew()
print("Skewness of Year:", skeness_year)
skeness_reviews = df['Reviews'].skew()
print("Skewness of Reviews:", skeness_reviews)
association_user_rating_genre = pd.crosstab(df['User Rating'], df['Genre'])
print("Association between User Rating and Genre:", association_user_rating_genre)
association_user_rating_price = pd.crosstab(df['User Rating'], df['Price'])
print("Association between User Rating and Price:", association_user_rating_price)