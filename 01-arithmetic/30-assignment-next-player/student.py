# write your code here

def next_player(player, player_count):
    if player < player_count - 1:
        n = player + 1
    else:
        n = 0
    return n