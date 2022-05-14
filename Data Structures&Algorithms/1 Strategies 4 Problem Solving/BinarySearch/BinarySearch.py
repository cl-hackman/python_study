# DIVIDE AND CONQUER: binary search is all about moving the mid bar through a sorted array
''' Grokking Algorithms     (A.E is another example)
BINARY SEARCH: is simply the means of getting closer to a target (with infinite search possibilities) by shortening 
the distance by 1/2
* It is sorted in ascending order unless rotated then, the low and high will have to be changed as in Assignment 4 in Binarysearchquestions.py
1.  This tool's tradeoff is that the elements in the Array have to be sorted otherwise it won't work
2.  It returns the element's position in the array or list that's why it needs sorting
3.  it's like searching for the word "xskssk" in an oxford dictionary. you start by openingm the book at the end so
you can get to all the X words. Then you will half the number of pages you will flip till you get the word. X becomes
your maximum bound or worst case (maximum number of operations to perform) or upper limit.
A.E: if someone asks you to guess a number they're thinking (you have 3 tries and they will tell you if your guesses are
too high or low), the number is in a list of 256 numbers, half 256 to 128, if the guessed number is too high, half again
to get 64. If it's too low, then you know the guessed number is in the range 128 to 64.
A simple search would be to guess all the numbers from 1 to 256 which would require O or 256 tries or operations.
A binary search would take log 2 N runtime because the base 2 is how we half the search, the N is the worst case (max N),
the answer (O) to it is the number of operations to be performed.
A.E: log 2 256(N) = 8(O): 8 operations (input) are needed to be performed inorder to solve this problemn in log runtime
'''  
# you've been given 3 to find in an array(vii). Binary search returns the index of 3 if it's in the array(vii)
# Using iterative procedure
def binary_search(x, item):
    low = 0 # list indexing starts with 0. len starts with 1 so -1 to get the last number
    high = len(x) - 1
    while low <= high:  # while low is less <= high, which is read as True so python starts looping in this boundary
        mid = int((low + high)/2)  #if result is a very number, it's stoarge could be an issue for the cpu so low+(high-low)/2 also works
        guess = x[mid]  # saying the element at the index x[mid]
        if guess == item: # if the item's index is equal to the index (x[mid])
            return mid    
        if guess > item: # if the index (x[mid]) is > than the item's index == mid is too high
            high = mid - 1   # start searching in the left side up to the new highest index(old mid -1)
        else:               # else, if guess<item, mid is too low 
            low = mid + 1   # search in the right side only starting from the new mid (old mid + 1)
    return None         # or the item doesn't exist

vii = [1, 3, 5, 7, 9]
print(binary_search(vii, 3)) # returns 1 the index position of 3 in vii
print(binary_search(vii, -1))   # returns None since it's not in the vii

# Using Recursive procedure (anything iterative can alson be recursed(acts like a while loop))
# Also runs in O(log2N) time
# no need for indexing
def Bsearch(Array, low, high, item):
    mid = int((low+high)/2)
    #pass a base case (like while low <= high in prev) so it breaks out otherwise it will loop forever
    if low > high:  # base case/condition 1
        return None
    elif item == mid: # base case 2
        return mid
    elif item > mid:      # in line 47, the previous mid+1 becomes the new lowest boundary
        return Bsearch(Array, mid+1, high, item)    # low becomes mid+1 meaning to search on the right side
    elif item < mid:      # this will make the search run once on either side not both sides
        return Bsearch(Array, low, mid-1, item)     # high becomes mid-1 meaning it searches on the left side
loo = [1, 3, 5, 7, 9]
print(Bsearch(loo, 1, 9, 7)) # returns 1 the index position of 3 in vii
print(Bsearch(loo, 1, 9, 9)) 

