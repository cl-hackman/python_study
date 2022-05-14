#For storinng large collection of data
#Dictionairies differ from Sets in that they take {Key : Value} whereas Sets don't. They both use curly brackets
#KEYS(input) : VALUES(output)
x=(33, 55, "dance", -33, 32.3)
y={1, 1, 2, 2, 3, 3, 4, 4, 5, 5}
z=["tim", 23, 322, 8.3, "harry"]
vii=dict(x=(33, 55, "dance", -33, 32.3), y={1, 1, 2, 2, 3, 3, 4, 4, 5, 5}, z=["tim", 23, 322, 8.3, "harry"])
print(vii)
#  Dicts are not Lists so they can't be edited using regular index like vii.index[0:3]
#You can the index STYle method to add stuff to the dictionary
vii["x"]=20
vii["z"]=2322 #why ["z"] becuase if you use [z], python will assume it to be a List thus it won't work well
print(vii)
#You can use in operator to find items in Keys of Dictionaries
if "10000" in vii:
    print(vii["10000"]) #Since 1000 is not in y, it prints nothing
    print(vii.get["10000"]) #  .get method prints None when there's nothing in the Dict 

print(vii.get('y', 0))

import pprint
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
coo = 0
def voo(A):
    for x in A:
        coo == coo.setdefault(x, 0)
        coo[x] = coo[x] + 1
    return coo

pprint.pprint(voo(inventory))


