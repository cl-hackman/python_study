letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 8], [8, 15]]
zeros = [0] * 6
combee = zeros + letters  # use + to concatinate list
print(combee)

numbers = list(range(20))  # list function is iterable. puts items in a list
print(numbers)

chars = list("hello world")
print(chars)
print(len(chars))

#ACCESSING ITEMS IN A LIST
letters = [2, 44, 56, 866, 22, 544346, 3323, 1, 2]
letters[0] = 67 #changing the first item in the list

print(letters[2]) #will print the 3rd item in the list
print(letters[-1]) #will print the item in the last position starting from the back
print(letters[0:4]) #OR print(letters[:4]): both will print the position of items in a form of a range


#TUPLES: Note- If you don't add BRACKETS to the data, python automatocally assumes it as a TUPLE 
chars = (1233, 34)  #can't modify elements in a tuple...it's great for keeping data unmodified..
tii = [4, 6, 7, 34]
vii = [9988, 55677, 8877, 33222]
lii = ["abq, defo, ghi, jkl"]
print(tii, vii, lii)        #Printing a group of variables
print(tuple(tii))       #tuple convertor takes only 1 argument
print(tuple(vii))
print(tuple(lii))