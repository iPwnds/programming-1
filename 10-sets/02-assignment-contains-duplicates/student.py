
def contains_duplicates(xs):
    if len(xs) == 0 or len(xs) == 1:
        return False
    else:
        xs.sort()
        ys = set(xs)
        ys = list(ys)
        ys.sort()
        if xs != ys:
            return True
        else:
            return False