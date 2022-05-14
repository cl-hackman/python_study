message = '''You are creating a fantasy video game. The data structure to model the player's inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value means the player has 1 rope, 6 torches, 42 gold coins, and so on'''

import pprint
i = {}
for x in message:
    i.setdefault(x, 0)  # in Dictionaries, setdefault() acts like append in Lits. It adds keys to i
    i[x] += 1 
pprint.pprint(i)