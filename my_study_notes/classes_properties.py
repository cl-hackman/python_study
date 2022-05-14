#Often use getter, setter, delete, and doc propeties so we can successfully make changes to our attributes 
#Propety method reduces the number of attributes we have in our code
#PROBLEM: I want to create an object to get prices and set them to only positive numbers
class Myownerror(Exception):    #This is how to create an exception for a class, THE NAME MUST END WITH "error". we are creating from the (Exception) class
    pass      
class Products:
    def __init__(self, prices, newprices): #You can print a statement here before the attribute.
        self.prices = prices #since self.new is a concatination of 2 attributes, we don't pass it as a parameter in our constructor
        self.newprice = newprices
        self.totalprices = prices + '.' + newprices #we use a getter so when we change self.prices (line 22), python will update the prices in self.new
    @property
    def prices(self):   #This initiates the get method: gets the values in our attributes so when we change it, python still recognizes it
        return self.prices 
        #to delete the value of an attribute, use the decorator @attribute.delete (attribute is the name of the object)
    @prices.setter    #we use the object name.setter
    def prices(self, value):#Setter allows user to set attributes to new values: here I am modfying my attribute to make them smart 
        if value > 1000 and value < 0:
            raise Myownerror("no negative prices") #You can type None instead of raising exceptions which is not suitable for large applications
        self.prices = value #Putting this statement under the if indentation makes python read it as Otherwise

vii = Products(20, 14)
vii.prices = 222 #setter property makes this change possible
print(vii.prices)



