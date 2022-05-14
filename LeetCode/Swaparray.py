# given an array of even and odd numbers, swap elements such that all even numbers come first and odd numbers come last

def even_odd(arr):
    next_even = 0   #left side
    next_odd = len(arr) - 1 #right side: moving down to the left
    # Brute Force approach
    while next_even < next_odd: # remember that this while loop will go through every element in the array
        if arr[next_even] % 2 == 0:
            next_even += 1  # add up from in a queue manner (from the left)
        else:
            # this is saying the left side (even_odd) becomes the right side (odd_number) and the right side becomes the left side
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1   # add up from the right 
    return arr


print(even_odd([1, 2, 3, 4, 5, 6]))
