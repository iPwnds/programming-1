# write your code here

from math import ceil

def internet_costs(duration_in_seconds, cost_per_block):
    cost = duration_in_seconds / 360
    cost = ceil(cost)
    cost *= cost_per_block
    return cost