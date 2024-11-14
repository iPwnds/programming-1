# write your code here

def subtuple(xs, ys):
    return not ys or any(xs[i:i + len(ys)] == ys for i in range(len(xs) - len(ys) + 1))
