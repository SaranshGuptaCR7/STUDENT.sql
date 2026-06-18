import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
df = load_breast_cancer()       
sns.set_style("dark")
import matplotlib as mlt
mlt.style.use(['https://gist.githubusercontent.com/BrendanMartin/01e71bb9550774e2ccff3af7574c0020/raw/6fa9681c7d0232d34c9271de9be150e584e606fe/lds_default.mplstyle'])
mlt.rcParams.update({"figure.figsize": (8, 6), "axes.titlepad": 22.0})
print("Target variables:", df['target_names'])
(unique, counts) = np.unique(df['target'], return_counts=True)
print("Unique values of the target variables", unique)
print("Counts of the target variables", counts)
sns.barplot(x=df['target_names'], y=counts)
plt.title("Target variables counts in dataset")
plt.show()