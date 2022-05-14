# Input Validation: using try block to make code run even after user inputs NON integer data type
print("how many cats do you have")
try:
    name = int(input()) #int here is going to convert only intergers placed in input() NOT input("six")
    if name >= 4:
        print("That's a lot of cats")
    elif name < 0:
        print("You kidding right")
except:
    print("Numbers Only")
    
# the try block helps our code run after it encounters an error
# You can use only except to take all kinds of error 
import os
vii = os.getcwd()
print(vii)