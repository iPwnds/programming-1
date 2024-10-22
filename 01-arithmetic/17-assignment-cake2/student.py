# write your code here

def cake2(eggs, flour):
    eggs_amount = eggs // 5
    flour_amount = flour // 250
    return min(eggs_amount, flour_amount)