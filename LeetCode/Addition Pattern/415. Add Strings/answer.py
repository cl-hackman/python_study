'''Initialize an empty res structure. Once could use array in Python and StringBuilder in Java.
Start from carry = 0.
Set a pointer at the end of each string: p1 = num1.length() - 1, p2 = num2.length() - 1.
Loop over the strings from the end to the beginning using p1 and p2. Stop when both strings are used entirely.
Set x1 to be equal to a digit from string nums1 at index p1. If p1 has reached the beginning of nums1, set x1 to 0.
Do the same for x2. Set x2 to be equal to digit from string nums2 at index p2. If p2 has reached the beginning of nums2, set x2 to 0.
Compute the current value: value = (x1 + x2 + carry) % 10, and update the carry: carry = (x1 + x2 + carry) / 10.
Append the current value to the result: res.append(value).
Now both strings are done. If the carry is still non-zero, update the result: res.append(carry).
Reverse the result, convert it to a string, and return that string.'''

num1 = "345"
num2 = "68889"
# my mistake: strings are not lists
'''
class Solution(object):
    def addStrings(self, num1, num2):
        res = 0
        {-since you don't know the number of times to loop through, it's best to use while loop here-}
        for i in num1:  
            i += i
            res += i
        for x in num2:
            x += x
            res+= x
            return res
'''

# From Youtube
# just as in everyday addition starting from right to left, we need a pointer that will move right to left
# but for linked lists, we don't need a pointer since there's a linked list class with val and next attributes which we can use to get the data directly from the nodes


def addStrings(num1, num2):
    res, carry = [], 0

    p1 = len(num1) - 1  # 1 string
    p2 = len(num2) - 1  # 2nd string
    while p1 >= 0 or p2 >= 0:
        # ord(x)-ord(0): ord returns the unicode value and subtracting it from ord(0) returns the integer value
        # else 0 says convert the digits but if there's no digit in a tenth, ones, etc, then set the space to zero
        x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
        x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
        value = (x1 + x2 + carry) % 10    # remainder on the right eg. 0 in 10
        carry = (x1 + x2 + carry) // 10   #remiander to the left eg. 1 in 10
        res.append(value)
        p1 -= 1  # since we're appending from the right side, we use p1 -=1 to track values or move pointer from the right
        p2 -= 1

    if carry:  # (if there's a value to carry)
        res.append(carry)

    # reverse answer
    # since we appended from the right we get eg. 001 instead of 100, so we use this to reverse
    return ''.join(str(x) for x in res[::-1])


print(addStrings(num1, num2))
