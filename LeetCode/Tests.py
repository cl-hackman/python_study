''' OBSERVATION:
In Recursion, after a function calls itself, the various stored return calls are added up {represented by return 0 and return 1 + x here} BACK 
to the main function call after the recursive calls meet the base condition or ground zero.
Therefore, set the ones you don't want to 0 and the ones you want to 1
When using Divide & Conquer in recursion, make sure the sub problem is of the same type as the major problem: if the problem is on sorting, 
then the sub problems you create should be of sorting as well
Note: you should have a method for combining all the sub solutions like return 1 + count(arr[1:], target)
Divide & Conquer strategy can be applied to all recursive algorithms like Binary Search, Merge Sort, etc.
'''
# 1. ADD all elements in an array

arr = [2, 4, 6, 9, 9, 9]
'''
my mistake
def sim(arr):  # using recursion
    if arr[:] == 1:
        return 1
    else:
        return arr[0] + arr[1:-1]
Note: arr[1:-1] returns second to last but one element in the list not second to last element
      arr[1:] returns the second to last element in the list

'''

# Correct recursive code


def sim(x):
    if x == []:  # BASE CASE
        return 0
    else:
        # the sim function is calling itself (this is the recursive part) till the base condition is met
        return x[0] + sim(x[1:])


print(sim(arr))


# USING iteration

'''
def total(x):
    sum = 0
    for y in range(len(x)):     # USE range(len()) or enumerate(x) when you want the index of the elements. Note len() is not range(len()). 
        sum += y
    return sum
'''


def total(x):
    sim = 0
    # x here works with the numbers themselves not the index as in range(len())
    for y in x:
        sim += y
    return sim


print(total(arr))

# 2. COUNT (like the len function does) the number of elements in a list using recursion


def sii(x):
    if x == []:
        return 0
    else:
        return 1 + sii(x[1:])


print(sii(arr))

# 3.  How many times a number occurs in an array?

# Check this link to better understand how regression call stacks work https://www.educative.io/collection/page/6151088528949248/4547996664463360/5639628738527232
arr = [2, 4, 6, 9, 9, 9]


def count(arr, target):
    # Base Case
    if arr == []:
        return 0

    # Recursive case1
    if arr[0] == target:
        # just like the tracker (total = 0, total += 1)
        return 1 + count(arr[1:], target)

    # Recursive case2
    else:
        return 0 + count(arr[1:], target)


print(count(arr, 9))

# 4. Find the first occurrence of a number using recursion: MY CORRECT CODE
ls = [2, 2, 4, 6, 9, 9, 9, 9]
target = 9


def occur(ls, target):
    if ls == []:
        return -1
    if ls[0] == target:
        return 0
    else:
        return 1 + occur(ls[1:], target)
        # [2, 2, 4, 6, 9, 9, 9, 9]]
        # [1, 1, 1, 1, 0] based on line 103-4
        # [1 + 1 + 1 + 1 + 0] adding up all the calls gives 4 if target is 9


print(occur(ls, 9))

# 5. 