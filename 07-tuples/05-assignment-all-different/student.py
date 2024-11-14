# write your code here

def all_different(xs):
    i = 0
    tot = 0
    while i < len(xs):
        if xs[i] in xs[i+1:]:
            return False
        else:
            tot += 1
        i += 1
    if tot == len(xs):
        return True