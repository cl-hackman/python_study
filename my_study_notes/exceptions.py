#these are codes written to tell the user what went wrong instead ofr python just shutting down
#Know the exceptions: python has a list of them
#to create one
try:
    file = open("file.py") #OR  With open("file.open") as x  since we use "with" statement (we can have more than 1 with statements as in opening more than 1 file), there's no need for finally except in some cases where with statement doesn't work
    age = int(input("input any number \n"))
    y = 1000 / age
except (ValueError, ZeroDivisionError) as x:  #as x means python will return the regular message in addition
         print(x) #Or "pass" (doesn't do anything)instead #exception: can take 1 or more objects WHEN in a bracket ()
        #Python will only run the first exception and ignore the other only if they're the same
else:   #this prints when there are no errors
    print("it's all good now")
finally:    # This executes regardless of anything
    file.close() 