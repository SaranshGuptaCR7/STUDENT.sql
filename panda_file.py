import pandas as pd
import numpy as np
exam_data = {'name': ['Leon', 'Rose', 'Miranda', 'Chris', 'Grace', 'Ethan', 'Mia', 'Virat Kholu', 'Thala', 'Kung Fu Pandey', 'Cristiano Ronaldo', 'Lionel Messi', 'Neymar'],
             'Score': [911, 14, 15, np.nan, 7, 70, 2, 150, 120, 711, 45, 54, np.nan],
             'Attempts': [1, 9, 7, 16, 18, 1500, 21, 27, 89, 29, 19, 7111, 9111],
             'Qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
df = pd.DataFrame(exam_data, index=labels)
print("Summary of the data in the DataFrame")
print(df)