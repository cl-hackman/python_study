'''Write a program that prints out the numbers 1 to 100 (inclusive). If the number is divisible by 3 print, Crackle instead of the number.
If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop. You can use any language you'''

import pprint
display = {}
for x in range(1, 100):
    # display.setdefault(x, '*')
    display[x] = "*"
    if x % 3 == 0:
        display[x] = 'Crackle'
    if x % 5 == 0:
        display[x] = 'Pop'
    if x % 3 and x % 5 == 0:
        display[x] = 'CracklePop'
pprint.pprint(display)
