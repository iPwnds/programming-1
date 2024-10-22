# write your code here

def middle(a, b, c):
    list = [a, b, c]
    list.remove(min(list))
    list.remove(max(list))
    return list[0]
    
