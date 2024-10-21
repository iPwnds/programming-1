# write your code here

def is_capitalized(string):
    if string == '':
        return False
    for i in string[1:]:
        if i == i.upper() and i != " ":
            return False
    if string[0] == string[0].upper():
        return True
    else:
        return False