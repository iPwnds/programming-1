# write your code here

def total_cost(amount):
    if amount < 100:
        fee = 10
        return amount + fee
    elif amount >= 200:
        discount = 0.95
        return amount * discount
    else:
        return amount