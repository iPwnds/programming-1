# write your code here

def passing_percentage(grades):
    pass_rate = 0
    fail_rate = 0
    for grade in grades:
        if grade >= 10:
            pass_rate += 1
        elif grade < 10:
            fail_rate += 1
    sum = pass_rate + fail_rate
    avg = pass_rate / sum
    return 100 * avg
