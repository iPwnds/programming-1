# write your code here

def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    eggs_amount = eggs // eggs_per_cake
    flour_amount = flour // flour_per_cake
    butter_amount = butter // butter_per_cake
    sugar_amount = sugar // sugar_per_cake
    return min(eggs_amount, flour_amount, butter_amount, sugar_amount)