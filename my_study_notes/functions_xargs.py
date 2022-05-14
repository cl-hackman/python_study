# "*" before y allows for many arguments to be set to a single parameter
def multiply(*y):       #Another way: def multiply(*numbers):, total = 1, for number in numbers: total *=x return total
    total = 1
    for x in y:
        total *= x #total = total * x
    return total


print("Hi")
print(multiply(3, 5, 7, 11,))

def fool(*yit):
    dance = 2
    for x in yit:
        dance *= x
    return dance

print(fool(6, 4, 5, 68, 63))


def one(*ulana):
    vee = 1
    for x in ulana:
        vee **= x
    return vee      #I have created a function that will always return 1 regardless of the multiple number-only arguments entered

print(one(95062, 34849404, 4866959, 83939292, 494394222, 9305890595953, 3383 ** 393))
print(one(-739393, 20944.4434, 0.823833473, -44449.24244, -872728424))




