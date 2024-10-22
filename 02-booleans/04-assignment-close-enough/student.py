# write your code here

def close_enough(x, y):
    if (y - 0.1) <= x <= (y + 0.1):
        return True
    else:
        return False