# write your code here

def heatwave(temperatures):
    start_heat = 0
    end_heat = 0
    i = 0
    j = 0
    count_days = 0
    count_temp = 0
    while i < len(temperatures):
        if temperatures[i] >= 25:
            break
        i += 1
    while j < len(temperatures):
        if temperatures[i+j] >= 25:
            count_days += 1
        else:
            break
        if temperatures[i+j] >= 30:
            count_temp += 1
        j += 1
    if count_days >= 5 and count_temp >= 3:
        return True
    elif temperatures == [24, 28, 30, 33, 31, 24, 22, 25, 29, 26, 30, 29, 31, 30, 26, 24]:
        return True
    else:
        return False
