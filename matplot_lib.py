import matplotlib.pyplot as plt
sales_data_ofalltime = [100, 150, 200, 250, 300, 911, 54, 711, 70]
sales_data_facecream = [50, 80, 120, 150, 200, 500, 30, 400, 20]
sales_data_facewash = [30, 60, 90, 120, 150, 400, 20, 300, 10]
company_profit = []
for i in range(len(sales_data_ofalltime)):
    profit = sales_data_ofalltime[i] - (sales_data_facecream[i] + sales_data_facewash[i])
    company_profit.append(profit)
def company_profit_plot():
    plt.plot(company_profit, label='Company Profit', marker='o')    
    plt.title('Company Profit Over Time')
    plt.xlabel('Time')
    plt.ylabel('Profit')
    plt.show()
company_profit_plot()
def comparitionof_cream_and_wash():
    plt.plot(sales_data_facecream, sales_data_facewash, label='Face Cream Sales', marker='o')    
    plt.title('Comparison of Face Cream and Face Wash Sales')
    plt.xlabel('Face Cream Sales')
    plt.ylabel('Face Wash Sales')
    plt.legend()
    plt.show()
comparitionof_cream_and_wash()