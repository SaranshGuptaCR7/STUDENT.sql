import matplotlib.pyplot as plt
blood_sugar_men = [90, 20, 56, 75, 811, 911, 34, 54, 67, 711, 920000, 2345, 1234, 5678, 8900]
blood_sugar_women = [120, 45, 543, 25, 7896, 911, 56, 78, 90, 1234, 5678, 8900, 2345, 6789, 3456]
type = [blood_sugar_men, blood_sugar_women]
colours = ['red', 'blue']
bins = [0, 100, 300, 500, 700, 900, 2000, 4000, 10000]
labels = ['Men', 'Women']  
plt.hist(type, bins=bins, color=colours, label=labels, orientation= 'horizontal', width=0.8, edgecolor='orange')
plt.title("Blood Sugar Levels Distribution", fontsize=14, fontweight='bold', fontfamily='verdana')
plt.xlabel("Blood Sugar Levels", fontsize=12, fontweight='bold', fontfamily='fantasy')
plt.ylabel("Total number of patients", fontsize=12, fontweight='bold', fontfamily='fantasy')  
plt.legend()
plt.show()