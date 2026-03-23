import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv('Tips_Dataset.csv')
def total_bill_distribution():
    sns.histplot(df['total_bill'], kde=True)
    plt.title('Distribution of Total Bill')
    plt.xlabel('Size')
    plt.ylabel('Tips')
    plt.show()
total_bill_distribution()
def histograph_of_total_bill():
    sns.histplot(df['total_bill'], kde=True)
    plt.title('Histogram of Total Bill')
    plt.xlabel('Total Bill')
    plt.ylabel('Frequency')
    plt.show()
histograph_of_total_bill()
def scatterplot_of_total_bill_and_tip():
    sns.scatterplot(x='total_bill', y='tip', data=df)
    plt.title('Scatter Plot of Total Bill vs Tip')
    plt.xlabel('Total Bill')
    plt.ylabel('Tip')
    plt.show()
scatterplot_of_total_bill_and_tip()
def pairplot_of_gender():
    sns.pairplot(df, hue='sex')
    plt.title('Pair Plot of Gender')
    plt.show()    