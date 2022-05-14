# WATCH [ TECH DOSE ] CHANNEL ON YOUTUBE: playlist called Concepts of Bitmasking
X_choice = True
Y_choice = False
Z_choice = True

choices = 0b111
# remember that 0 is a falsy value
# Bit masking or masking Bits is blocking the unwanted variables by setting them to zero
print(choices & 0b100)  # set the other variables to zero to get X_choice
print(choices & 0b010)  # set the first and last variable to zero to get Y_choice
print(choices & 0b001)  # set the first and second variables to zero to get Z_choice

# shifiting
#if x = 0b110110011
x = 0b110110011
print(x) # x = 435
# shifiting happens here
y = x << 20  # saying add twenty zeros (since  its less than <<) to the end of the binary value in x
print(bin(y))
z = x >> 4  # saying remove the four elements at the end of x 
print(bin(z))

'''
>>> 16 << 1 ## 16 shifted left once = 16 * 2
32
>>> 16 << 2 ## 16 shifted left twice = 16 * (2 * 2)
64
10000 ## 16 in binary
10000 << 1 ## shift left once
100000 ## Returns 32 in binary, we have shifted one bit to the left

10000 ## 16 in binary
10000 << 2 ## shift left twice
1000000 ## returns 64 in binary, we have shifted 2 bits to the left
'''
