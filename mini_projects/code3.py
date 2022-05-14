# FOR LOOPS are while loops that end; range(1(start), 10(end)), 2(step): range(1, 10, 2) even numbers to 10

#Create a program that asks for Username 4 times as it notifies user the number of attempts left then locks when last attempt is reached
# For Loop is generally BAD for this project
try:
    name = ""
    for x in range(1, 5):  
        if name != "Collins":
            print("Enter Username:")
        name = input()
        if x == 1:
            print("3 attempts remaining")
        if x == 2:
            print("2 attempts remaining")
        if x == 3:
            print("1 attempt remaining")
        if x == 4:
            print("Account Locked")
        else:
            if name == "Collins":
                print("Welcome Collins")
                break
except:
    pass
