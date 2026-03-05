import numpy as np
data_type = [('name', 'S15'), ('class', 'int'), ('height', 'float')]
student_details = [
    ('Leon', 12, 5.9),
    ('Grace', 10, 5.5),
    ('Ashley', 10, 5.5),
    ('Chris', 12, 5.8),
    ('India vs New Zealand', 9, 5.6)
]
students = np.array(student_details, dtype=data_type)
print("Original Array:")
print(students)
print("Sort by height")
print(np.sort(students, order='height'))