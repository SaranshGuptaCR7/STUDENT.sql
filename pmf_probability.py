import scipy.stats as stats
prob_a = stats.binom.pmf(2, 10, 0.5)
print("The probability of getting exactly 2 heads in 10 trials is:", round(prob_a, 4))
prob_b = stats.binom.pmf(3, 10, 0.5)
print("The probability of getting exactly 3 heads in 10 trials is:", round(prob_b, 4))
prob_total = prob_a + prob_b
print("The probability of getting either 2 or 3 heads in 10 trials is:", round(prob_total, 4))