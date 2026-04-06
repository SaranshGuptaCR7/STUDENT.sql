import matplotlib.pyplot as plt
import seaborn as sns
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
births = [12, 15, 11, 9, 1, 9, 21]
month1 = [10, 12, 8, 6, 0, 7, 18]
month2 = [14, 18, 12, 10, 2, 11, 25]
plt.plot(day, births, marker='o', color='blue')
plt.title("Births by Day of the Week", fontsize=16, fontweight='bold', fontfamily='arial')
plt.xlabel("Day of the Week", fontsize=12, fontweight='bold', fontfamily='cursive')
plt.ylabel("Number of Births", fontsize=12, fontweight='bold', fontfamily='cursive')
plt.show()
days1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
birth1 = [17, 5, 2, 11, 1, 9, 29]
plt.plot(days1, birth1, marker='o', color='red')
plt.title("Births by Day of the Week in August", fontsize=16, fontweight='bold', fontfamily='arial')
plt.xlabel("Day of the Week", fontsize=12, fontweight='bold', fontfamily='cursive')
plt.ylabel("Number of Births", fontsize=12, fontweight='bold', fontfamily   ='cursive')
plt.show()
def barplot_of_birth_rate():
    sns.barplot(x=month1, y=month2)
    plt.title('Bar Plot of Birth Rate', fontsize=16, fontweight='bold', fontfamily='arial')
    plt.xlabel('Month 1', fontsize=12, fontweight='bold', fontfamily='cursive')
    plt.ylabel('Month 2', fontsize=12, fontweight='bold', fontfamily='cursive')
    plt.legend()
    plt.show()
barplot_of_birth_rate()    