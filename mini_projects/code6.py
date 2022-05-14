# Assignment Code Comma
spam = ['apple', 'bananas', 'tofu', 'cats'] 
spin = "hello my name is Collins okrrrrr"
def stringer(a):    #Created a fucnction that will convert a list of strings into a single string with "and" b4 the last value
     return ', '.join(a[0:-1]  + ["and" + " " + a[-1]]) 
     ''' the join() will pass the "," on the left in the spaces of the list of strings on the right.
     You can join a list of strings using the + as well'''
     '''The .split() will convert a string statement into a list of string. Whatever you put in the right side will be
     "delimited" '''
print(spin.split("okrrrrr"))
print(stringer(spam))
print(spin.partition("my"))
print(spin.rjust(30))
print(spin.ljust(20, "-"))


