# write your code here

def cake3(eggs, flour, butter, sugar):
    eggs_amount = eggs // 5
    flour_amount = flour // 250
    butter_amount = butter // 200
    sugar_amount = sugar // 250
    return min(eggs_amount, flour_amount, butter_amount, sugar_amount)