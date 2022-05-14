# enumerate func gives a numerate obj in a topple: it gives the index of objects in the lisr
letters = ["a", "b", "c", "d", "e"]
jump, cow, *others = letters
for jump, cow in enumerate(letters):
    print(jump, cow)
