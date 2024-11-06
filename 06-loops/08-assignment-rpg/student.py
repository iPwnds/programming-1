
def rpg2(n_sides, goal):
    count = 0
    for i in range(n_sides):
        for j in range(n_sides):
            sum = j+i
            if sum >= goal:
                count += 1 
                print(count)
    return count / (n_sides**2)

# Not yet solved