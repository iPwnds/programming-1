def product(a, b, c):
    if a == None and b == None and c == None:
        return 1
    elif a == None and b == None:
        return c
    elif a == None and c == None:
        return b
    elif b == None and c == None:
        return a
    elif a == None:
        return b * c
    elif b == None:
        return a * c
    elif c == None:
        return a * b
    else:
        return a * b * c