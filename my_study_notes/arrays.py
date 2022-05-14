# part of Data Structures (collection of data to make coding experience smoother)
# it's like lists but for larger sets of data, it's more preferale of the two
# Arrays are very good for collecting data streams (a collection raw data coming from a source like social media analysis, etc that is transformed into user friendly data)  )

from array import array #Array module
vii = array("i", [1, -1, 7, -2, 3, -3]) #if you add any other data type like a string/float to the list, the array will not work: [1, -1, 8.33]
zii = array("f", [6.82, 83.3, 8.22, 33.23, 90.11, 15.57, 31.89])
zii[0] = 2.34
vii[2] = -225
vii.append(78)
vii.insert(0, 67)
vii.pop(-2)
print(zii)
print(vii)
"python" #neglect this
#swap variables in Python
x = 1, 2, 33, 54, "Anna"    #Remember that no (), python will read as a TUPLE
y = 55.4, 763.24, 543.33, 53, 22, -12
y, x = x, y  #use the list unpacking style
print(y, x)