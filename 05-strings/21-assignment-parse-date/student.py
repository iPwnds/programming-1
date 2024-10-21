# write your code here

def parse_day(string):
    if string[0] == 0:
        string = string[1]
        return int(string)
    else:
        string = string[0] + string[1]
        return int(string)

def parse_month(string):
    if string[3] == 0:
        string = string[4]
        return int(string)
    else:
        string = string[3] + string[4]
        return int(string)

def parse_year(string):
    string = string[6] + string[7] + string[8] + string[9]
    return int(string)