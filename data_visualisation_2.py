import matplotlib.pyplot as plt
x = [1, 4, 25, 34, 56, 70, 91, 11]
y = [1, 42, 26, 14, 86, 10, 15, 17]
y1 = [0, 40, 29, 38, 46, 77, 98, 21]
plt.plot(x, y, color='blue', marker='o', label='Velocity 1')
plt.plot(x, y1, color='red', marker='o', label='Velocity 2')
plt.title('Velocity Comparison' , fontsize=12, fontweight='bold')
plt.xlabel('Time (s)', fontsize=12, fontweight='bold')
plt.ylabel('Velocity (m/s)', fontsize=12, fontweight='bold')
plt.legend()
plt.show()
