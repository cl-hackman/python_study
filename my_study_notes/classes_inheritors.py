#I CREATED THIS CODE BY MYSELF...NO COPY :)
#we have similar methods under various classes in many codes
#we don't want to keep creating the same methods all over again in various codes so we use inheritors
# DRY: DONT REPEAT YOURSELF: create an abstract class instead
#class Combined(Company, Place): #Multiple Inheritance/P multiple Parent classes: usually bad practice
        #pass
#Multi level inheritance is not good practice because if there are similar methods in different classes, inherting them is bad


class Place:    #Parent Class
    def county(self):
        return "Bronx"

class Company(Place):  #SUB CLASS: Inheriting the county method from the Place class
    def __init__(self, x):
        pass
    def companyname(self, x):
        return x.lower()

class Offices(Place):   
    def office_buildings(self):
        return 25

vii = Company("TMOBILE")
voo = Offices()
print(vii.county()) #Now, we're using the county method from the Place class in our Company class a.k.a vii
print(vii.companyname("TMOBILE"))
print(voo.office_buildings()) #remember voo is the variable representing our object Offices

