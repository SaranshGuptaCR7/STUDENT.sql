import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
df = pd.read_csv('country_vaccinations.csv')
df.head(10)
df.isnull().any()
subset = df.iloc[:5200, :]
plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.show()
df.head(10)
df.dropna(how="all")
df.bfill()
df.interpolate()
df_dropped = df.dropna()
df_dropped