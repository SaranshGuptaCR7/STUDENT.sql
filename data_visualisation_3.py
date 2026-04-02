import matplotlib.pyplot as plt
import pandas as pd
countries = pd.read_csv('Countries_Data.csv')
C_52 = countries.loc[countries['year'] == 1952]
C_07 = countries.loc[countries['year'] == 2007]
C_merge = C_52.merge(C_07, left_on='country', right_on='country')
C_merge = C_merge.drop(['year_x', 'year_y'], axis=1)
C_merge['population_growth'] = C_merge['population_y'] - C_merge['population_x']
C_merge = C_merge.sort_values('population_growth', ascending=False).head(10)
names = C_merge['country']
pop_growth = C_merge['population_growth'] / (10**6)
plt.figure(figsize=(15, 9))
plt.bar(names, pop_growth, width=0.6, color='orange', edgecolor='red')
plt.xlabel("Countries", fontsize=12, fontweight='bold')
plt.ylabel("Population Growth (in millions)", fontsize=12, fontweight='bold')
plt.title("Top 10 Countries with Highest Population Growth (1952-2007)", fontsize=14, fontweight='bold', fontfamily='cursive')
plt.xticks(rotation=190)
for x, y in zip(names, pop_growth):
    label = "({:.2f})".format(y)
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')
plt.show()    