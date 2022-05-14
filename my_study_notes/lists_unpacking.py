# unpacking lists into variables
# setting variables to a variable with lists
hello = [1, 2, 3, 4, 5]
a, b, c, d, e = hello
print(a)
# Alternatively;
hello = [1, 2, 3, 4, 5]
first = hello[0]
second = hello[1]
third = hello[2]
fourth = hello[3]
fifth = hello[-1]
print(first, fourth)

# the "*" before others allows to set to many objects in a list
hello = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
a, *b, c = hello
print(a, c)
print(*b, c)
print(b, c)