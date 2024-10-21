# write your code here

def is_student_id(string):
    index = 0
    if len(string) == 8:
        if string[0] == "R" or string[0] == "r" or string[0] == "S" or string[0] == "s":
            for i in string[1:]:
                if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
                    index += 1
                else:
                    return False
            if index == 7:
                return True
            else:
                return False
        else:
            return False
    else:
        return False