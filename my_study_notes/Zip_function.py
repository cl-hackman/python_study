# just combining two or more lists or iterables into a single list 
# since zip function is iterable, you can pass strigns and other objects along with the list
x = [1, 2, 3]
y = [10, 20, 30]

print(list(zip([y, x])))
print(list(zip("abc", x, y)))  #can passing it with a string or other iterables
 