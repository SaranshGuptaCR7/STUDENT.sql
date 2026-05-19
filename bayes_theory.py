def find_prob(a, b):
    if a == 1:
        prob_a = 0.2
        if b == 1:
            prob_bga = 0.85 
        elif b == 2:
            prob_bga = 0.15
        else:
           print("Invalid Choice")
        prob_a_and_b = prob_a * prob_bga
        print("Probability of b given that a:", prob_bga)
        print("Probability of a and b:", prob_a_and_b)
    elif a == 2:
        prob_a = 0.8
        if b == 1:
            prob_bga = 0.02
        elif b == 2:
            prob_bga = 0.98
        else:
            print("Invalid Choice")
        prob_a_and_b = prob_a * prob_bga
        print("Probability of b given that a:", prob_bga)
        print("Probability of a and b:", prob_a_and_b)
    else:
        print("Invalid Choice")
print("Calculate the probability of the events")
print("DO the person has a step throat?\n1. Yes\n2. No")
a = int(input("Enter your choice(1/2): "))
print("DO the person has tested positive?\n1. Yes\n2. No")
b = int(input("Enter your choice(1/2): "))
print("Probability of a and b:")
find_prob(a, b)