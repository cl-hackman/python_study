age = input("how old are you? \n ")
answer = int(age)
message = "eligible" if answer >= 18 else "not eligible"
print(message)
message_2 = "automatically enrolled" if 34 <= answer < 65 else "hi human"
print(message_2)

# you can summarize conditional statements into a vraiable
# instead of following the notes under "conditional_statements" file, create a variable and set it = to the conditional statements
