''' 
Given an array of integers nums sorted in non-decreasing order, find the STARTING and ENDING position of a given target 
value. If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.'''
# Correct
def bSearch(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:  # while low is less than high, let's start running
        mid = int((low+high)/2)
        guess = nums[mid]
        if guess == target: # in the original binary search, we would have stopped here since it's goal is to discard other parts
            low = mid   # by doing this, we're saying wherever search for mid == target in both the left and right sides 
            high = mid
            #the two while loops is going to make python search the left & right sides otherwise, it will return only mid if it = target
            while low >= 0 and nums[low-1] == target: # saying mid > 0 and nums[mid-1]: pyhton should search in the left range
                low -= 1    # keep track of the index target if it falls in the low region
            while high < len(nums)-1 and nums[high+1] == target: # saying mid < lens(num)-1 and nums[mid+1]: python should search in the max to min range on the right 
                high += 1   # keep track of the index target if it falls in the high regin
            return [low, high]  # this gets us out of the while loop and returns the lowest no. in min range and highest no. in max range
        elif guess < target:    # this part is not necessary but it's for the 2 while loop sake otherwise, it will run in a mess
            low = mid+1
        else:
            high = mid-1
    return [-1, -1]

xii = [1, 1, 2, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11, 11]
print(bSearch(xii, 11))