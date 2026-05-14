def prob_a_and_b(a, b, total):
    prob_a = orange/total
    prob_b = blue/(total - 1)
    pron_inter = prob_a * prob_b
    return round(pron_inter, 7)
print("Check the probability of any event occuring. First enter your choices:")
orange = int(input("Enter the number of orange balls: "))
blue = int(input("Enter the number of blue balls: "))
total = orange + blue
print("Here s' the probability of the events", prob_a_and_b(orange, blue, total))
