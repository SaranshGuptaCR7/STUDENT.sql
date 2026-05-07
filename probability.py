import random
import matplotlib.pyplot as pd
import seaborn as sns
balls = ['red', 'yellow', 'blue']
pro = random.choice(balls)
result = balls.count('red')/len(balls)
if pro == 'red':
    print("Red ball is selected")