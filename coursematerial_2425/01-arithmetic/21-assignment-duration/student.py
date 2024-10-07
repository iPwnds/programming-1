# write your code here

def hours(duration):
    return duration // 3600

def minutes(duration):
    h = hours(duration)
    minutes = duration - (3600 * h) 
    return minutes // 60

def seconds(duration):
    h = hours(duration)
    minutes = duration - (3600 * h) 
    m = minutes // 60
    seconds = minutes - (60 * m)
    return seconds