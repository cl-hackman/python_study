count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1  # so as x is divided by 2, this condition will keep increasing by 1 for count since it's placed under the if statement
        print(x)    # placing the count condition under the if statement is called SCOPE
print(f"we have {count} numbers")
 
# the following is a mistake
for numbers in range(1, 12):
    vee = numbers % 2 == 0  # not a conditional statement
print(f"we have 4 {vee} numbers")
