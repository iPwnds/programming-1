# write your code here

def box(string):
    length = '--'
    for i in string:
        length += '-'

    return("+" + length + "+\n"
          "| " + string + " |\n"
          "+" + length + "+")