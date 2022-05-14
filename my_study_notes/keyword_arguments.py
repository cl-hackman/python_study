# used to make code clearer and to make an argument optional

def increment(number, by=1):
    return number + by
# number is a positional argument

print(increment(3))
#no need for a second argument since by is made optional thanks to setting it to by=1 (a keyword (default) argument)

