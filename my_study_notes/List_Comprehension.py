#no need for map and filter functions and lambda
#viit = [expression or condition, for x in viit if, and, or, not clause can be added] #no need for list()
yoott = [-7, -3, -99, -16, -4, -2, -5, -11, -12, -43, -77, 3, 4, 66, 13, 5, 67, 8, 23, 54, 99, 11, 32, 77, 12, 41, 14, 28]
kii = [x ** 2 * 3.1415 for x in yoott if x <= 15]
mii = [x // 4 for x in yoott if x % 2 == 0 and x // 1]  #if the and operator's boolean is True, it will work
zii = [x * 2 * 3.1415 for x in yoott if x != x % 2 == 0]
print(kii)
print(mii)
print(zii)
#no need for map function filter function, list function, or lambda


# exclusive to python, it performs the task of map (changing lists) and filter (picking out) functions
# note, map and filter function works on only 1 list at a time
gyals = [
    ("Product1", 10),
    ("Product3", 9),
    ("Product2", 17),
]

# for map function
prices = [x[0] for x in gyals]
print(prices)

# for filter function
prices_only = [x for x in gyals if x[1] >= 10]
print(prices_only)

#Filter for only movie names starting with G 
#Filter for movies made before year 2000
movies = [("Star Wars", 1941), ("Ghandi", 2001), ("Casablanca", 1978), ("Shawhank", 2000), ("Toy Story", 2017), ("Gone With The Wind", 2006), ("Citizen Kane", 1941), ("It's a Wonderful Life", 1996), ("The Wizard and Oz", 2011)("Gattaca", 1993), ("Rear Window", 1994), ("Ghostbusters", 1981), ("Groundhug Day", 2002), ("To Kill A Mockingbird", 1921), ("Good Will Hunting", 2014), ("2001: A Space Odyssey", 2019), ("Raiders of The Lost Arc", 1998), ("Close Encounter of The Third Kind", 2005)]
lii = [x for x in movies if x[0] == "G"]
kii = [x[0] == "C" for x in movies] #returns only false so switch the condition to the end using an if statement: Check the 1st List Comprehension
zii = [x for x in movies if x[1] <= 2000]
print(lii)
print(kii)
print(zii)
