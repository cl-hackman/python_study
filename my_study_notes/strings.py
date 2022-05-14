time = "Too late"
print(len(time))
print(time[0])
print(time[0:3])
print(time[:])
time = "Too \"late"
print(time)
time = "Too \\late"
print(time)
time = "Too \nlate"
print(time)
time = 'Too "late'
print(time)
first = "Collins"
middle = "Asiedu"
last = "Hackman"
full_name = f"{first} {middle} {last}"
print(full_name)
collins = "  god colliginins "
print(collins.upper())
print(collins.lower())
print(collins.title())
print(collins.strip())
print(collins.find("ins"))
print(collins.replace("l", "d"))
print("col" in collins)
print("dance" not in collins)
print("mar" in collins)
print(collins.strip())
#can't begin with a number
#specialized characters ($) are not allowed

first = "harry"
last = "jose"
full = f"{first} {last}"
print(full)
print(f"{first} {last}") 
print("joe" + " " + "mary") #concantenation
