# write your code here

def parse_position_x(string):
    string = string[1:len(string) - 1]
    i = 0
    while len(string) > i:
        if string[i] == ",":
            index = i
        i += 1
    result = string[:index - 1]
    return int(result)

def parse_position_y(string):
    string = string[1:len(string) - 1]
    i = 0
    while len(string) > i:
        if string[i] == " ":
            index = i
        i += 1
    result = string[index:]
    return int(result)