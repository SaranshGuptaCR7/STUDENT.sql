import pandas as pd
import matplotlib.pyplot as mlt
import seaborn as sns
import numpy as np
df = pd.read_csv('IMBD_Dataset.csv')
df.head(3)
df.tail(3)
df.info()
df.describe()
df.isnull().sum()
df.isnull(type='any')
subset = df.iloc[41, 75]
def boxplot_of_IMDB_Rating_and_Runtime():
    sns.boxplot(x='IMDB_Rating', y='Runtime', data=df)
    mlt.title('Box Plot of IMDB Rating')
    mlt.xlabel('IMDB Rating')
    mlt.ylabel('Runtime')
    mlt.show()
boxplot_of_IMDB_Rating_and_Runtime()
def scatterplot_of_IMDB_Rating_and_Runtime():
    sns.scatterplot(x='IMDB_Rating', y='Runtime', data=df)
    mlt.title('Scatter Plot of IMDB Rating and Runtime')
    mlt.xlabel('IMDB Rating')
    mlt.ylabel('Runtime')
    mlt.show()
scatterplot_of_IMDB_Rating_and_Runtime()
def countplot_of_Content_Rating():
    sns.countplot(x='Content_Rating', data=df)
    mlt.title('Count Plot of Content Rating')
    mlt.xlabel('Content Rating')
    mlt.ylabel('Count')
    mlt.show()
countplot_of_Content_Rating()           