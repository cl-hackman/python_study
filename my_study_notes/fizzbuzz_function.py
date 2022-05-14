

def fizz_buzz(xee):
    if (xee % 3 == 0) and (xee % 5 == 0): #For 15
        return "FizzBuzz"
    if xee % 3 == 0:
        return "Fizz"
    if xee % 5 == 0:
        return "Buzz"
    return xee
# if not 3, 5, and 15, condition will be false so the same x number will be returned automatically. No code needed again

print(fizz_buzz(5))



