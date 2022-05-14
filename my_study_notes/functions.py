#USING LAMBDA (No name functions or anonymous functions) & MAP
yoott = [4, 5, 3, 5, 7, 8, 9, 3, 24, 34, 98, 6, 21, 12, 11, 9, 18]
viit = list(map(lambda x: x **2 * 3.1416, yoott))     #(a function called x: condition, yoott)
print(viit)
kii = list(filter(lambda x: x >= 999, viit))
print(kii)

#OR can create a function that will take an input
yoott = [4, 5, 3, 5, 7, 8, 9, 3, 24, 34, 98, 6, 21, 12, 11, 9, 18]
def area(x):
    yoott = x ** 2 * 3.14159265359
    return yoott

print(area(4))


def power(x):
    return x * x
print(power(26887688998657558543765))




# parameters or arguments can be any defined object like strings or integers and others
# The two purposes of functions are 1.perform a task and 2.to calculate and return a value


def sassy(x):
    return (f"Hello {x}")


print(sassy("gummy bear"))


def odd_number(boy):
    return (2 * boy + 1)


print(odd_number(15))


# keyword argument makes the code readeable
# can use default arguments: setting parameter by as optional after the required parameter number)

def odd_number2(number, by=1):  #two parameters
    return (2 * number - by)


print(odd_number2(18))
print(odd_number2(3, 17))

def even_number(number):   #one parameter
    return(2 * number)


print(even_number(14))


