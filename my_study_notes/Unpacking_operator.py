#You want to unpack elements in a container like string, tuple, class, list, dictionary
#use *
gii = ("at", 5, 33, -4843)  #can be a Tuple or any other
print(gii)
print(*gii, *"Killango la Tete")


#exercise_frequency.py original answer from codewithmosh
import collections
dii = "This is an interview question"
zoo = collections.defaultdict(int)      #This method with (int) will convert the string into a dictionary of iterable intergers for the calc.
for x in dii:
    zoo[x] += 1
print(sorted(zoo.items(), key=lambda x: x[1], reverse=True)[0])