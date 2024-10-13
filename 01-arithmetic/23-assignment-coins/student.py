# write your code here

def coins(amount):
    euro5 = amount // 5
    amount -= euro5 * 5
    
    euro2 = amount // 2
    amount -= euro2 * 2

    euro1 = amount // 1

    return euro5 + euro2 + euro1