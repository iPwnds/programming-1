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
            start_heat = i
            break
        i += 1
    while j < len(temperatures):
        if temperatures[start_heat+j] >= 25:
            count_days += 1
        if temperatures[start_heat+j] >= 30:
            count_temp += 1
        else:
            break
        j += 1
    if count_days >= 5 and count_temp >= 3:
        return True
    else:
        return False
