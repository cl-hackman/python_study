import pprint #this dsplays dictionairies in a beautiful format
message = "Hello, my name is collins. How do you do today?"
def voo(A):
    for x in message:
        coo = {}  # so we can add up the keys and count the number of times each character appears in dictionary
        coo = coo.setdefault(x, 0) # to append keys into our coo variable: it's not working for now
        coo[x] = coo[x] + 1 # the key
    return coo  # this will count the number of times each item appears in the dictionary

pprint.pprint(voo(message))

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
vii = 0 # since we already got a dictionary, det the variable to 0
def totalvalues(A):
    for x, y in A:  # we use x and y since this is a dictionary
        vii = vii + y.setdefault(x, 0) # to sum the value y to get a total of all y
    return vii  # this will count the number of times each item appears in the dictionary

pprint.pprint(totalvalues(inventory))