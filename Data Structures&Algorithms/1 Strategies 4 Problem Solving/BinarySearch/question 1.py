# Assignment: how many times does 5 occur? if there's no 5, return [-1, -1]
xii = [1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11, 11]
# My wrong code: i didn't work with the indices of all x in the array
'''def bSearch(array, low, high, x):
        occ = 0   # occ is occurence
        mid = int((low+high)/2)
        if low > high:
            return None
        if x == mid:
            occ += 1 
        if x > mid:
            low = mid + 1
            occ += 1
        if x < mid:
            high = mid - 1
            occ += 1
        return occ 
print(bSearch(xii, 1, 11, 9))'''

xii = [1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11, 11]

# 2nd attempt:
'''def bSearch(array, x):
    low = 0
    high = len(array) - 1
    occurence = 0
    while low <= high:
        mid = int((low+high)/2)
        guess = array[mid]
        if guess == x:
            occurence += 1
        if guess > x:
            high = mid - 1
            occurence += 1
        if guess < x:
            low = mid + 1
            occurence += 1
            return occurence
print(bSearch(xii, 3))'''
#Correct
def occurrence(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:  # while low is less than high, let's start running
        mid = int((low+high)/2)
        guess = nums[mid]
        if guess == target: # in the original binary search, we would have stopped here since it's goal is to discard other parts
            low = mid   # by doing this, we're saying wherever search for mid == target in both the left and right sides 
            high = mid
            #the two while loops is going to make python search the left & right sides otherwise, it will return only mid if it = target
            while low >= 0 and nums[low-1] == target: # saying mid > 0 and element at the index nums[mid-1]: pyhton should search target in the left range
                low -= 1    # keep track of the INDEX target if it falls in the low region
            while high < len(nums)-1 and nums[high+1] == target: # saying mid < lens(num)-1 and element at the index [mid+1]: python should search in the max to min range on the right 
                high += 1   # keep track of the INDEX target if it falls in the high regin
            return [high-low+1]  # this gets us out of the while loop: since we tracked the index of the target (lines77&79), we need to add one to get the accurate count since list indexing begin with 0 to -1
        elif guess < target:    # this part is not necessary but it's for the 2 while loop sake otherwise, it will run in a mess
            low = mid+1
        else:
            high = mid-1
    return [-1, -1]

occ = [1, 1, 2, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11, 11]
print(occurrence(occ, 2))

# Assignment 4:
'''
There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly 
rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1],
..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. Given the array nums 
after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity
'''
'''
* My problem was: I didn't know that binary search sorting requires that the elements be sorted in ascending order
unless ROTATED *
My Mistake:
def sott(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = int((high+low)/2) # this is 3
        guess = nums[mid]       # is nums[3]: the mid (3) is now the index
        if guess == target:
            low = mid + 1
            low += 1
            return [low]
        else:
            return [-1, -1]'''

