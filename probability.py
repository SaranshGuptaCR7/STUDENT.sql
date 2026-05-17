def prob(totaal, a):
    prob_a = a / totaal
    totaal = 6
    return prob_a
    if prob_a == 6:
        print("The game has started")
    else:
        print("The game has not started") 
print("The probability of getting six is:", prob(6, 1))        