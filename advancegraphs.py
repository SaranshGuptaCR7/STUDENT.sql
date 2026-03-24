import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('Iris_Dataset.csv')
def barplot_of_species_and_sepal_length():
    sns.barplot(x='species', y='sepal_length', data=df)
    plt.title('Bar Plot of Species and Sepal Length')
    plt.xlabel('Species')
    plt.ylabel('Sepal Length')
    plt.show()
barplot_of_species_and_sepal_length()
def countplot_of_species():
    sns.countplot(x='species', data=df)
    plt.title('Count Plot of Species')
    plt.xlabel('Species')
    plt.ylabel('Count')
    plt.show()    
countplot_of_species()
def boxplot_of_species_and_sepalwidthcm():
    sns.boxplot(x='species', y='sepal_width', data=df)
    plt.title('Box Plot of Species and Sepal Width')
    plt.xlabel('Species')
    plt.ylabel('Sepal Width')
    plt.show()
boxplot_of_species_and_sepalwidthcm()
def swarmplot_of_species_and_sepalwidthcm():
    sns.swarmplot(x='Species', y='Sepal Width', data=df)
    plt.title('Swarm Plot of Species and Sepal Width')
    plt.xlabel('Species')
    plt.ylabel('Sepal Width')
    plt.show()
swarmplot_of_species_and_sepalwidthcm()
def pairplot_of_species():
    sns.pairplot(df, hue='Species')
    plt.title('Pair Plot of Species')
    plt.show()
pairplot_of_species()