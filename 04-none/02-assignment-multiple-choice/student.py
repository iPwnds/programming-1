def multiple_choice(right_answer, given_answer):
    if given_answer == None:
        return 0
    elif given_answer == right_answer:
        return 1
    elif given_answer != right_answer:
        return -0.2
    