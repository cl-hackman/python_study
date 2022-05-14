# int(x)
# float(x)
# bool(x)
# str(x)

j = input("enter birth year: ")
k = 2021 - int(j) + 1
print(f"your age is {k} in actual present value terms starting from 0 BC")

# MINI TYPE CONVERTORS
# ord(x):: takes a single string character and converts it to a Unicode value. Subtract the ord(x) from ord(0) to get the integer value
# chr(x):: takes an integer and converts it to a string value

z = ord("g") + 1
q = chr(66) + "e"
print(z)
print(q)
