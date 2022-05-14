''' While loops will execute the code and return to the while clause (condition) and iterate all over again
for loops just repeats iterable objects where as while loops repeats a task after evaluating a condition
Ctrl + C breaks the while loop in the terminal or we can use a "break" condition
if statements are logical statements like rectangles in flow charts, they evaluate to boolean expressions'''

# CREATING MY OWN PROGRAM TO ASK FOR USERNAME AND PASSWORD JUST LIKE LOGIN PORTALS ON WEBSITES DO:::
try:
    name = "" #We = "", 0, 0.0 so python knows "name" and to set the condition to True otherwise we get error, and to not take an empty input
    while name != "Collins":    #Python sets the condition to True since "" in line 6 is read as False by default
        print("Enter Username") #So the user get a statement before the input 
        name = input()
        continue   # Continue will return us to the block if the input is evaluated to be True (not Joe)
    if name == "Collins":   #Since name == Collins, the 1st while loop is evaluated to False so python moves to the next condition and based on its indentation, it seprat
        print("Welcome Collins")
        print("Now! Enter password")
        while True: #Infite loop because we set it to be always True so if line 16 is True, it will loop line 17 till it becomes True
            password = input()
            if password != "1997*":
                print("Try again")
            elif password == "1997*":
                break
    print("Access granted")
except:
    pass
    #NB: "" (Falsy value for Strings), 0 (Falsy value for integer), 0.0 (Falsy value for floats)
