numbers = [3, 55, 11, 33, 7, 21]
# to sort items in lists in ascending order
numbers.sort()
print(numbers)

# the "sort" method has 2 parameters, key and reverse

# to sort in descedning order use reverse
numbers.sort(reverse=True)

# another one is "sorted" function

print(sorted(numbers))
print(sorted(numbers, reverse=True))

# sort works for numbers only so use lamda functions : eg. girls.sort(key=lambda parameters: expression)

items = [
    ("product A", 189),
    ("product C", 555),
    ("product D", 4736),
    ("product E", 7866),
    ("product B", 378),
]  # using topples (complex objects like strings + numbers) in lists
# python can't sort the list above due to its topple and string nature. Instead of creating a function, "lambda" is used
# as an ananymous function

items.sort(key=lambda items: items[1])
print(items)


# MAP FUNCTION : To change the format of lists
# to change the list of food proccessing orders to prices only:
# rather than create a function:

prices = []  # empty set so we can apend items into this variable list
for x in items:
    prices.append(x[1])

print(prices)

# MAP FUNCTION is easier
vaah = list(map(lambda x: x[1], items))
print(prices)

#you can also use map function to apply a function to a set of data like  applying a lambda (anonymous function) to a set of data
# Check Socratica YouTube video on map, filter,......