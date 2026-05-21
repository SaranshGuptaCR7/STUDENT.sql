import scipy.stats as stat
prob_1 = stats.binom.cdf(6, 10, 0.5)
print("The probability of getting at most 6 heads is:", round(prob_1, 1))
print(prob_1)