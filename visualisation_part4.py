import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('Penguins_Data1.csv')
bins = [0, 10, 20, 30, 40, 50]
plt.hist(data['Body Mass (g)'], bins=bins, color='cyan', edgecolor='black')
plt.title('Histogram of Body Mass', fontsize=16, fontweight='bold', fontfamily='arial') 
plt.xlabel('Body Mass (g)', fontsize=12, fontweight='bold', fontfamily='cursive')
plt.ylabel('Frequency', fontsize=12, fontweight='bold', fontfamily='cursive')
plt.show()

plt.hist(data['Culmen Length (mm)'], bins=bins, color='cyan', edgecolor='black')
plt.title('Histogram of Culmen Length', fontsize=16, fontweight='bold', fontfamily='arial') 
plt.xlabel('Culmen Length (mm)', fontsize=12, fontweight='bold', fontfamily='cursive')
plt.ylabel('Frequency', fontsize=12, fontweight='bold', fontfamily='cursive')
plt.show()

plt.hist(data['Culmen Depth (mm)'], bins=bins, color='cyan', edgecolor='black')
plt.title('Histogram of Culmen Depth', fontsize=16, fontweight='bold', fontfamily='arial') 
plt.xlabel('Culmen Depth (mm)', fontsize=12, fontweight='bold', fontfamily='cursive')
plt.ylabel('Frequency', fontsize=12, fontweight='bold', fontfamily='cursive')
plt.show()

plt.hist(data['Flipper Length (mm)'], bins=bins, color='cyan', edgecolor='black')
plt.title('Histogram of Flipper Length', fontsize=16, fontweight='bold', fontfamily='arial') 
plt.xlabel('Flipper Length (mm)', fontsize=12, fontweight='bold', fontfamily='cursive')
plt.ylabel('Frequency', fontsize=12, fontweight='bold', fontfamily='cursive')
plt.show()