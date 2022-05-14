
# Classes are useful for storing functions that help users run our code easily with no background knowledge
# We use a constructor/special method (__int__) to create an object with multiple parameters. 
# Python reads the SELF as our Dance object, x, y, z are our parameters
# Objects are the variations of the user input or data we assign to a class
# Methods tell us how to use the Object
# Methods are used for {performing separate actions whereas Attributes are used to store the data
# placed into our object for re-use}
# Since Methods are known as Procedual Attributes, they take at the end, Attributes don't take ()
# e.g: a.age is an attribute, a.get_age() is a method
# we do this __self.x to our attributes to hide them fron ourside influence
class Employees:   #this follows Pascal naming convention: the opposite of the variable naming and every first letter is capitalized
    the_company = "NBA"  #Class Object is a default object which doesn't change regardless of codes

    def __init__(self, name, race, gender):
        self.x = name     # Attributes: Instead of this, they can be added later, check Dance.k = 23
        self.y = race  #self.y is saying that you want the 1st data (x) from our Dance (self) object
        self.z = gender
        self.xy = name + '.' + race + '@gmail.com'

    def __str__(self):  #A magic method which python how present our code otherwise you will get that __main object..... statement
        return f"({self.x}, {self.y}, {self.z})"
        
    @classmethod    #A decorator. Classmethods are suitable if you have complex arguments you want to repeat using
    def lala(self):
        return dict(black_employees= 150000)

    def __str__(self):  #A magic method which returns the object as a string its same as str()
        return f"({self.x}, {self.y}, {self.z})"

    def namegender(self):   # Use '{} {}'.format() to return statement (line 32) as a Dictionary
        return '{} {}'.format(self.x, self.y)  #We can assign object attributes in a Method
#We can use default methods in the return section
#You can set a condition to the Method before the return (line 20)
#We can add many magic methods that perform certain conditions and allow us to perform operations like ADD objects

vii = Employees("Kofi", "black", "male")   # Object: Dance
voo = Employees.the_company
Employees.year = 2021    #adding attributes: its safer using the property function(getter & setter)in another file
print(vii)
print(vii.x)           #Here python replaces vii as "self" in our __init__
print(vii.xy)
print(voo)
print(vii.year) 
print(vii.namegender()) #for the variable, no argument needed since python reads self for our method's argument
print(Employees.namegender(vii))    #for the object, we need to pass the variable as our argument
zii = Employees.lala()
print(zii) 
print(vii.x)




