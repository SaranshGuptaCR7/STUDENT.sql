import pandas as pd
import numpy as np
df = pd.read_csv("glass.csv")
print(df.head(5))
print(df.dtypes)
print(df.info())
target = df.iloc[:, -1]
print("\nTarget variables name:", df.columns[-1])
unique, counts = np.unique(target, return_counts=True)
print("\nUnique values in target variables:", unique)
print("Counts of the target variables:", counts)
if len(unique) == 2:
    print("\nThe target variable is binary.")
else:
    print("\nThe target variable is multi-class.")
if len(unique) == 2:
    print("\nComment: The dataset has two target classes, which means it is binary")
else:
    print("\nComment: The dataset has", len(unique), "target classes, which means it is multi-class")   