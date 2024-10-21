# write your code here

def palindrome(string):
    i = 0
    newString = ''
    while len(string) > i:
        newString += string[(-1 - i)]
        i += 1
    if string == newString:
        return True
    else:
        return False