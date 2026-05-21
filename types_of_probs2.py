import scipy.stats as stat
prob_1 = stat.poisson.pmf(6, 10)
print("The probability of raining exactly 6 events is:", round(prob_1, 1))
prob_2 = stat.poisson.pmf(12, 10) + stat.poisson.pmf(13, 10) + stat.poisson.pmf(14, 10)
print("The probability of raining for 12-14 days is:", round(prob_2, 1))