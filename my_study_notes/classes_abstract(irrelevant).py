# This is NOT NECESSARY other than for conventional good inheritance practice sake
# It's not good practice to keep using the same methods with different actions when inheriting classes
# However, to make our code appear smoother it's best to do so safely by Using abstract classes
# Our code will run smoothly even without abstracting the class or method
# We can either abstract the class alone or method alone
        #Example
# We are going to collect a stream of data from a file and network (we read them differently)
from abc import ABC, abstractmethod
# from the abstract (abc) module, import the abstract (ABC) class
class Invaliderror(Exception):
    pass
class Stream(ABC): #We create this abstract class to make a common code which we will inherent in sub classes
    def __init__(self):
        self.opened = False #We use the booleans to say that when a File/Network is OPENED or CLOSED, do this
    def open(self):
        if self.opened:
            raise Invaliderror("stream is already opened")
        self.opened = True #The indentation under the if column makes ptyhon read this line as "otherwise"
    def closed(self):
        if not self.opened:
            raise Invaliderror("stream is already closed")
        self.opened = True 
    @abstractmethod #This makes read our abstractmethod thus safely resuing it throughout all sub classes
    def read(self): # WE pass nothing here
        pass
#Since we read the File/Network stream differently, let's create sub classes for them
class FileStream(Stream):
    def read(self):
        print("Reading Data from File stream")
class NetworkStream(Stream):
    def read(self):
        print("Reading Data from Network stream")
class MemoryStream(Stream): #we need to repeat the read method here otherwise python will assume it as another abstract class
    def read(self):
        print("Reading from Memory stream")

# THIS PART IS RELEVANT: to pass a group of objects as a list in a function.
# The function has to be a common method for all the classes 
def read(controls): #this is not a method belonging to the classes
    for x in controls:    #so we can our classes in a list--line 49
        x.read()


vii = FileStream()
voo = NetworkStream()
vee = MemoryStream()
print(vii.read())
print(voo.read())
print(vee.read())

read([vii, voo])