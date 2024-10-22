# write your code here
from math import ceil

def movie_ticket(duration, imax, student, ticket_count):
    if duration <= 90:
        price = 10
    elif 90 < duration <= 120:
        price = 11
    elif 120 < duration <= 150:
        price = 12
    elif 150 < duration:
        price = 15
    if imax:
        price = ceil(price * 1.2)
    if student:
        price -= 3
    
    price = price * ticket_count
    return price