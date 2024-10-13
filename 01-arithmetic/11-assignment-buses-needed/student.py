# write your code here

from math import ceil

def buses_needed(people_count, bus_capacity):
    buses = people_count / bus_capacity
    return ceil(buses)