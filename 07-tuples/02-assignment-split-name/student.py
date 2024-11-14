# write your code here

def split_name(full_name):
    space = 0
    i = 0
    while i < len(full_name):
        if full_name[i] == " ":
            space = i
        i += 1
    return (full_name[:space], full_name[space+1:])