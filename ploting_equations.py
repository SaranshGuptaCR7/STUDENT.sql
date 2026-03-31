import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 11, 1)
y = (2 * x) + 1
y1 = (2*x**x) + 1
plt.plot(x, y, color='blue', marker='o', label='Linear Equation 1')
plt.plot(x, y1, color='red', marker='o', label='Exponential Equation 2')
plt.title('Plotting Equations' , fontsize=12, fontweight='bold')
plt.legend()
plt.show()