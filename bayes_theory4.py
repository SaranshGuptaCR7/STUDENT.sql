import scipy.stats as stats
x = 3
n = 10
prob_1 = stats.binom.pmf(x, n, 0.5)
print("The probability of getting exactly 3 heads is:", round(prob_1, 1))
print(prob_1)
prob_2 = 1-stats.binom.pmf(0, n, 0.5) - stats.binom.pmf(1, n, 0.5) - stats.binom.pmf(2, n, 0.5)
print("The probability of getting more than 2 heads is:", round(prob_2, 1))
print(prob_2)