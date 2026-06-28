import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
df = load_breast_cancer()
x = df.data
y = df.target
(unique, counts) = np.unique(y, return_counts=True)
print("Target Names:", df.target_names)
print("Unique Values:", unique)
print("Counts:", counts)
if len(unique) == 2:
    print("\nThe target variable is binary.")
else:
    print("\nThe target variable is multi-class.")    
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
model = LogisticRegression(max_iter=10000)
model.fit(x_train, y_train)
predicted = model.predict(x_test)
accuracy = accuracy_score(y_test, predicted)
print("Comment: The Breast Cancer dataset is a Binary Classification dataset because it has", len(unique), "target classes (Malignant and Benign). The Logistic Regression model achieved an accuracy of", accuracy)