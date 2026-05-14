rs = int(input("Enter the number of red shirts:"))
bs = int(input("Enter the number of blue shirts:"))
ws = int(input("Enter the number of white shirts:"))
total = rs + bs + ws
prob_a = bs/total
prob_b = rs/total
prob_bga = prob_b
prob_inter = prob_a * prob_b
print("Probability that the second shirt is red given that the first shirt is blue:")
print(round(prob_bga, 9))
print("Probability that the second shirt is red and the first shirt is blue:")
print(round(prob_inter), 11)