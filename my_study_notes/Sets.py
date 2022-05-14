#   Sets are data structure types that removes duplicates. They're represented with {}.
#   They are great for MATH operations
vii = [1, 1, 2, 2, 4, 4 -55, -55, -344, -344, -22, -22]
x=set(vii)  #pretty cool huh: no need for brackets 
print(x)

zii=(1, 322, 44, 1, 33, -98, -54)
y=set(zii)
y.add(748)
print(y)

print(x|y)  # | add sets
print(x & y)  # & finds the intersections in the sets
print(x-y)  # - finds the difference between the sets
print(x^y)  # ^ (carrot) finds the compliments 
#For Sets, we can't use the index method(zii.index[0]) because they're UNORDERED collections so we us the IN operator 
if 33 in y: #To check if 33 is in y
    print(y)
