# Using a greedy algorithm approach
def boat_func(): 
    a = [1, 2, 4, 6, 7]
    a.sort()
    limit = 2
    boat = 0
    l, r = 0, len(a)-1  # two pointers: one to move from left and the other to move from right
    while l<=r:
        remain = limit - a[r]
        r -= 1  # take it out
        boat += 1   # and put it here
        if l <= remain > a[l]:
            l += 1
    return boat

print(f"You can have {boat_func()} boats of people")
