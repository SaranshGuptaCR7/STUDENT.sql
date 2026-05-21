import scipy.stats as stats
prob_1 = stats.poisson.cdf(20, 15)
print(round(prob_1, 9))
prob_2 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)
print((round(prob_2, 9)))