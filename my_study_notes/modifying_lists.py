numbers = [1, 3, 5, 7, 11, 13, 23]
numbers.append(17)  # adds only a single item to the list
numbers.append(19)
numbers.append(29)
numbers.insert(0, 87)   #(index or position, x-value)
numbers.pop(2)  # removes an item in the list based on its position
numbers.remove(23)
del numbers[0:3]
print(numbers)
