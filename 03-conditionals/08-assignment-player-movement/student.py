# write your code here

def player_movement(position, left_arrow, right_arrow, shift):
    if shift:
        if left_arrow and right_arrow:
            return position
        elif left_arrow:
            return position - 2
        elif right_arrow:
            return position + 2
        else:
            return position
    elif shift == False:
        if left_arrow and right_arrow:
            return position
        elif left_arrow:
            return position - 1
        elif right_arrow:
            return position + 1
        else:
            return position
    else:
        return position