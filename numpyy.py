import numpy as np
data_type = [('Name', 'String'), ('Age', 'int'), ('Class', 'int'), ('Height', 'float')]
students = np.array([('John', 20, 11, 5.8), ('Alice', 22, 7, 5.5), ('Bob', 19, 12, 6.0)], dtype=data_type)
print("Original array:", students)
print("Sort by class:", np.sort(students, order='Class'))
print("Slicing of data:", students[1:3])