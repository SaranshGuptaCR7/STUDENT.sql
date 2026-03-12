import pandas as py
import numpy as np
employee_details = {'Name': ['Rohit', 'Suresh', 'Ramesh', 'Sanjay'], 
 'Age': [25, 30, 35, 40], 
 'Department': ['HR', 'IT', 'Sales', 'Marketing']}
employee_df = py.DataFrame(employee_details, index=['Emp1', 'Emp2', 'Emp3', 'Emp4'])
labels = ['*', '*', '*', '*']
print(employee_df)