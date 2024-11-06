# write your code here

def sum_input():
    user = 0
    while 1 > 0:
        user_input = int(input("Enter integer: "))
        if user_input == 0:
            break
        user += user_input
    user = str(user)
    print("The sum equals " + user + ".")