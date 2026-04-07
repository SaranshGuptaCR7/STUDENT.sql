import matplotlib.pyplot as plt
import seaborn as sns
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
births = [12, 15, 11, 9, 1, 9, 21]
days1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
birth1 = [17, 5, 2, 11, 1, 9, 29]
month1 = [10, 12, 8, 6, 0, 7, 18]
month2 = [14, 18, 12, 10, 2, 11, 25]
def barplot_of_birth_rate1():
    sns.barplot(x=day, y=births)
    plt.barplot(x=days1, y=birth1, color='yellow', width=0.4, edgecolor='orange')
    plt.title('Bar Plot of Birth Rate', fontsize=16, fontweight='bold', fontfamily='arial')
    plt.xlabel('Day of the Week', fontsize=12, fontweight='bold', fontfamily='cursive')
    plt.ylabel('Number of Births', fontsize=12, fontweight='bold', fontfamily='cursive')
    plt.legend()
    plt.show()
barplot_of_birth_rate1()
def barplot_of_birth_rate2():
    sns.barplot(x=day, y=births)
    plt.barplot(x=days1, y=birth1, color='orange', width=0.4, edgecolor='yellow')
    plt.title('Bar Plot of Birth Rate', fontsize=16, fontweight='bold', fontfamily='arial')
    plt.xlabel('Day of the Week', fontsize=12, fontweight='bold', fontfamily='cursive')
    plt.ylabel('Number of Births', fontsize=12, fontweight='bold', fontfamily='cursive')
    plt.legend()
    plt.show()   
barplot_of_birth_rate2() 
def barplot_of_birth_rate_2months():
    sns.barplot(x=month1, y=month2)
    plt.barplot(x=month1, y=month2, color='purple', width=0.4, edgecolor='blue')
    plt.title('Bar Plot of Birth Rate', fontsize=16, fontweight='bold', fontfamily='arial')
    plt.xlabel('Month 1', fontsize=12, fontweight='bold', fontfamily='cursive')
    plt.ylabel('Month 2', fontsize=12, fontweight='bold', fontfamily='cursive')
    plt.legend()
    plt.show()
barplot_of_birth_rate_2months()    