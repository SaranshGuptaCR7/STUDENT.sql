import numpy as where
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from collections import Counter
X,y = make_blobs(n_samples=1000, centers=2, random_state=1)
print(X.shape, y.shape)
counter = Counter(y)
print(counter)
for i in range(10):
    print(X[i], y[i])
for label, _ in counter.items():
    row_ix = where(y == label)[0]
    plt.scatter(X[row_ix, 0], X[row_ix, 1], label=str(label))
    plt.legend()
    plt.show()    