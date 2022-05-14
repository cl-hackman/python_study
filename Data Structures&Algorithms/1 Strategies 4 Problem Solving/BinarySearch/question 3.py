# Assignment 4:
'''
There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly 
rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1],
..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. Given the array nums 
after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity
'''
# My mistake:
'''
My problem was: I didn't know that binary search sorting requires that the elements be sorted in ascending order
unless ROTATED *
def sott(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = int((high+low)/2) # this is 3
        guess = nums[mid]       # nums[3]: is the NUMBER/ELEMENT at the index 3
        if guess == target:
            low = mid + 1
            low += 1
            return [low]
        else:
            return [-1, -1]'''

# Read this:
''' The issue here is that the array is sorted in decreasing order not ascending (traditional for binary search)
so  the low has become the high and the high has become the low therefore, how do you let python know this?
we're not searching for the occurence of elements here so we make changes to the original code in (question 1.py) not 
the one in (question 2.py)'''

# WATCH THIS ON YOUTUBE TO understand better: ''' https://www.youtube.com/watch?v=U8XENwh8Oy8 '''

# Correct from leetcode: 
def sott(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = int((low+high)/2)
        guess = nums[mid]   # is going to give me the number in the index nums[mid]
        if guess == target:
            return mid
        if guess > target:
            if low <= guess and nums[low] > target: #nums[0] is 4 in the array
                low = mid + 1 #look on the right side
            else:
                high = mid - 1
        if guess < target:
            if nums[low] > nums[mid] and nums[low] <= target:   # <= target is very important 
                high = mid - 1
            else:
                low = mid + 1
    return [-1, -1]

kii = [4,5,6,7,0,1,2] 
print(sott(kii, 0))
