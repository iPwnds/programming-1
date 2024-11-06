# write your code here

def thanos(queue_size, target_size):
    i = 0
    while queue_size > target_size:
        queue_size = queue_size // 2
        i += 1
    return i 