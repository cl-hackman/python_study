''' 
In base 10, 1423 is calcualted as 1 x 10^3 + 4 x 10^2 + 2 x 10 + 3 * 10^0. we get 1423 just like in 1x1000 + 4x100 + 2x10 + 3
In binary, we use base 2 so 0bn1011100 (obn is binary) is converted to base 10 by: 
1 x 2^6 + 0 x 2^5 + 1 x 2^4 + 1 x 2^3 + 1 x 2^2 + 0 x 2^1 + 0 x 2^0
we get 92 in base 10 value''' 
d= 0b1011100
print(d) # d is 92

#bitise operations AND, OR, XOR work like boolean values 'AND, OR, NOT'
# bitwise and---we use &
x = 2 & 3
'''if both binary values are 1, write 1 if not write 0'''
print(bin(x))
print(bin(3))
print(bin(2))

#bitwise or---we use |
'''if either is 1, we write 1'''
y = 4 | 6
print(bin(y))
print(bin(4))
print(bin(6))

#bitwise XOR---we use ^
'''if one value is 1 but not both are 1 (opposite of &, close to |)'''
z = 7 ^ 9
print(bin(z))
print(bin(7))
print(bin(9))


