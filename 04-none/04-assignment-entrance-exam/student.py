def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    grade = [grade1, grade2, grade3, grade4, grade5]
    counter = 0
    amount = 0
    for i in grade:
        if i == None:
            counter += 1
        else:
            amount += i

    if counter > 1:
        return False
    else:
        total = amount / (5 - counter)
        if total < 12:
            return False
        else:
            return True