# Want to display a column of keys on the left with values on the right
movies = {"Star Wars": 1941, "Ghandi": 2001, "Casablanca": 1978, "Shawhank": 2000, "Toy Story": 2017, "Gone With The Wind": 2006, "Citizen Kane": 1941, "It's a Wonderful Life": 1996, "The Wizard and Oz": 2011, "Gattaca": 1993, "Rear Window": 1994, "Ghostbusters": 1981, "Groundhug Day": 2002, "Rush": 1921, "Good Will Hunting": 2014, "A Space Odyssey": 2019, "Noah's Arc": 1998, "Exodus": 2005}

print("inventory display")
def column(movietitles, Keys2theleft, Values2theright): 
    print("Movies".center(Keys2theleft + Values2theright, "="))
    for k, v in movietitles.items():
        print(k.ljust(Keys2theleft, ".") + str(v).rjust(Values2theright)) #concatenation
print(column(movies, 20, 5))

'''.rjuts(10, "*") is saying, push the string 10 spaces to the left and put * as the spaces'''
'''the y2theleft is the number of space that the user will enter for the .rjust method and the z2theleft is the number 
of space the user will enter for the .ljust method'''