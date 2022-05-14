class Person:
    '''This is a Person Class. It has printname and changename methods'''

    species = "Homo sapiens sapiens"

    def __init__(self, fname, lname):
        self.__firstname = fname
        self.__lastname = lname

    def printname(self):
        print(self.__firstname, self.__lastname)

    def changename(self, fname, lname):
        self.__firstname = fname
        self.__lastname = lname
        print("Sucessfully changed")


Sonyl = Person("Sonyl", "Nagale")
# print('hello')
David = Person("David", "Gantt")
Sonyl.printname()
David.printname() 