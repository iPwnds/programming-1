
def remove_empty_lines(source, destination):
    newString = ''
    with open(source, 'r', encoding='utf-8') as file:
        string = file.readlines()
        for i in string:
            if i != '\n':
                newString += i

    with open(destination, 'w', encoding='utf-8') as file:
        file.write(newString)