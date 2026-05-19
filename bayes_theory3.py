import numpy as np
die_sides = int(input("Enter the number of sides on the die(6/12): "))
die = range(1, die_sides)
num_rolls = int(input("Enter the number of rolls: "))
result = np.random.choice(die, size = num_rolls, replace = True)
print("Results of the dice rolls:", result)