evens = {2, 4, 6}
greater_than_two = {3, 4, 5, 6}
all_outcomes = {1, 2, 3, 4, 5, 6}
def prob_a_and_b(a, b, outcomes):
    prob_a = len(a) / len(outcomes)
    prob_b = len(b) / len(outcomes)
    inter = a.intersection(b)
    prob_inter = len(inter) / len(outcomes)
    return(prob_a + prob_b - prob_inter)
print(prob_a_and_b(evens, greater_than_two, all_outcomes))