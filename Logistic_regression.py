import numpy as np
from sklearn.linear_model import LogisticRegression
x = np.arange(10).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
model = LogisticRegression()
model.fit(x, y)
predicted = model.predict(x)
print("Predicted values:", predicted)