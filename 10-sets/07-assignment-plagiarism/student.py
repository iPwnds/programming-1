
def plagiarism(s1, s2):
    s1 = s1.split()
    s2 = s2.split()
    result = 0
    old = set()
    for i in s1:
        for j in s2:
            if i == j and i not in old:
                result += 1
                old.add(i)
    return result