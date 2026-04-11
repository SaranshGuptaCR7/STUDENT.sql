import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data = pd.read_csv('Penguins_Data1.csv')
data.head()
data.info()
data.columns
sns.scatterplot(x= 'Body Mass (g)', y='Culmen Length (mm)', data=data, color='cyan', edgecolor='black', s=100, marker='o')
plt.title('Scatter Plot of Body Mass vs Culmen Length', fontsize=16, fontweight='bold', fontfamily='arial')
plt.xlabel('Body Mass (g)', fontsize=12, fontweight='bold', fontfamily='cursive')
plt.ylabel('Culmen Length (mm)', fontsize=12, fontweight='bold', fontfamily='cursive')
plt.show()  

sns.scatterplot(x= 'Body Mass (g)', y='Culmen Depth (mm)', data=data, color='cyan', edgecolor='black', s=100, marker='o')
plt.title('Scatter Plot of Body Mass vs Culmen Depth', fontsize=16, fontweight='bold', fontfamily='arial')
plt.xlabel('Body Mass (g)', fontsize=12, fontweight='bold', fontfamily='cursive')
plt.ylabel('Culmen Depth (mm)', fontsize=12, fontweight='bold', fontfamily='cursive')
plt.show()  
 
sns.pairplot(data, x_vars=['Body Mass (g)'], y_vars=['Culmen Length (mm)', 'Culmen Depth (mm)', 'Flipper Length (mm)'], height=5, aspect=1.5, color='red', edgecolor='black', s=100, marker='o')
plt.title('Pair Plot of Body Mass vs Culmen Length, Culmen Depth, and Flipper Length', fontsize=16, fontweight='bold', fontfamily='arial')
plt.show() 