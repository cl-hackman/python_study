#Parent Classes' cnstructors overiding the constructer in the Sub Class leading to methods overiding
# super().__init__() : This prevents that by passing the parent constructor separate from the method's
#Overridng affects the attributes
class Place:  #Parent Class
    def __init__(self, zone): 
        self.zone = zone    #for teaching method override sake, I put a constructor here

    def county(self, z):
        if z != "Bronx":
            raise ValueError("Permision denied: only Bronx allowed")
        elif z == "Bronx":
            print("Access granted")

class Company(Place):  #Inheriting the county method from the Place class
    def __init__(self, area):
        self.area = area  
        super().__init__() #This won't let the parent class attribute override the sub classes'
    def companyname(self, x):
        return x.lower()

vii = Company("TMOBILE")
print(vii.county("Bronx")) #Now, we're using the county method from the Place class in our Company class a.k.a vii
print(vii.companyname("TMOBILE"))
print(vii.area)
