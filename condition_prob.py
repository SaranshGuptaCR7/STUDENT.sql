def a_and_b(a, b):
    if a == 1:
        prob_student = 0.7
        if b == 1:
           prob_dinning = 0.75
        else:
          prob_dinning = 0.25
        print("Probability of a given by b:", prob_dinning)

    if a == 2:
        prob_student = 0.7
        if b == 1:                
           prob_dinning = 0.6
        else:
           prob_dinning = 0.4
        print("Probability of a given by b:", prob_dinning)
    prob_a_and_b = prob_student * prob_dinning
    return round(prob_a_and_b, 7)
print("Check the probability of any event occuring. First enter your choices:")
print("Is the student Freshman? \n1. Yes \n2. No")
a = int(input("Enter your choice for a: "))
print("Is the student eating in the dinning hall? \n1. Yes \n2. No")
b = int(input("Enter your choice for b: "))
print("Here s' the probability of the events", a_and_b(a, b))