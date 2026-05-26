import scipy.stats as stat
prob_1 = stat.poisson.pmf(12, 10)
print("The probability of raining exactly 12 days is:", round(prob_1, 1))
prob_2 = stat.poisson.pmf(13, 10) + stat.poisson.pmf(14, 10) + stat.poisson.pmf(15, 10) + stat.poisson.pmf(16, 10) + stat.poisson.pmf(17, 10) + stat.poisson.pmf(18, 10) + stat.poisson.pmf(19, 10) + stat.poisson.pmf(20, 10) + stat.poisson.pmf(21, 10) + stat.poisson.pmf(22, 10) + stat.poisson.pmf(23, 10) + stat.poisson.pmf(24, 10) + stat.poisson.pmf(25, 10) + stat.poisson.pmf(26, 10) + stat.poisson.pmf(27, 10) + stat.poisson.pmf(28, 10) + stat.poisson.pmf(29, 10) + stat.poisson.pmf(30, 10)
print("The probability of raining for 12-30 days is:", round(prob_2, 1))
prob_3 = stat.poisson.pmf(13, 10) + stat.poisson.pmf(14, 10) + stat.poisson.pmf(15, 10) + stat.poisson.pmf(16, 10) + stat.poisson.pmf(17, 10)
print("The probability of raining for 12-18 days is:", round(prob_3, 1))