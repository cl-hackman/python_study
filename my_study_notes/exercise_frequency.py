
# My Failed Attempt
vii = "This is a common interview question"
zii = {x: vii.count(x) for x in vii}
#Dict. Comprehension: X is the Key/Input & vii.count is the Output/Condition of the no. of time x occurs. The For loop defines our Key/Input X)
print(zii)
# THE ONES BELOW ARE FROM STACK OVERFLOW
#To find the most occuring letter
from collections import Counter 
fii = Counter("This is a common interview question")    #Counter is going to count each element in fii and display it as a dictionary
print((fii).most_common(1)[0])  #put the mousepad point over the methods to know what they do. The most_common method works with Counter class
#Or
from collections import defaultdict  #Necessary for python to know which module and subclass I want 
dii = "This is an interview question"
zoo = defaultdict(int)  #This object with (int) will convert the string into a dictionary of iterable intergers for the calc.
for x in dii:
    zoo[x] += 1
print(sorted(zoo.items(), key=lambda x: x[1], reverse=True)[0])     
#Or
import collections
fii = Counter("This is a common interview question")
print(collections.Counter(fii).most_common(1)[0])   #The [0] will remove the [] on our answer
