# write your code here

def increasing(ns):
    i = 1
    count = 0
    if len(ns) == 0:
        return True
    while i < len(ns):
        if ns[i-1] > ns[i]:
            return False
        else:
            count += 1
        i += 1
    if count+1 == len(ns):
        return True