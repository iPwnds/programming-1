
def remove_duplicates(xs):
    ys = set()
    result = []
    for i in xs:
        if i not in ys:
            result.append(i)
            ys.add(i)
    return result