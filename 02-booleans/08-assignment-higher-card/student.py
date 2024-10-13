# write your code here

def higher_card(card1, card2):
    if card1 > card2 and card1 != 1 and card2 != 1:
        return True
    elif card1 == card2:
        return False
    elif card1 == 1:
        return True
    elif card2 == 1:
        return False
    else:
        return False