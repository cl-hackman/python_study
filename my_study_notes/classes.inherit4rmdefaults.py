#Note that the changes made to the default class pertain to this file and code only
class Mystring(str):    # str is a default class (they come in lowercase)
    def addup(self): # creating a method to extend the uses of the default string class
        return self + self

print(Mystring("hello world").addup())

#modifying the use of a default method in a default class
class Mylist(list): #list is the default class
    def append(self, x):    #add a parameter so python knows you're modifying the default method
        print("append completed")
        super().append(x)   #super() is representative of the parent class


list = Mylist()
list.append(24)
