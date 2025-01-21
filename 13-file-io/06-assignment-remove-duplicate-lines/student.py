
def remove_duplicate_lines(source, destination):
    newString = ''
    oldString = ''
    with open(source, 'r', encoding='utf-8') as file:
        string = file.readlines()
        for i in string:
            if i not in oldString:
                oldString += i
                newString += i

    with open(destination, 'w', encoding='utf-8') as file:
        file.write(newString)