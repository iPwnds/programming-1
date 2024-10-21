# write your code here

def tip_calculator():
    price = int(input("Enter total price: "))
    tip = input("Enter tip percentage (default=20): ")

    if tip == '':
        total = int(price * 1.2)
        print(f"You have to pay {total}")
    else:
        total = int(price * (1 + (int(tip) / 100)))
        print(f"You have to pay {total}")