xade = input("enter any number: \n")
y = int(xade)
if (y % 3 == 0) and (y % 5 == 0):
    print("fizzbuzz")
if y % 3 == 0:      #no need for elif since condition is similar
    print("fizz")
if y % 5 == 0:
    print("buzz")

