
def find_duplicates(xs):
    ys = set()
    zs = set()
    result = []
    for i in xs:
        if i in ys:
            if i not in zs:
                result.append(i)
                zs.add(i)
        else:
            ys.add(i)
    return result