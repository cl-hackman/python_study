import pprint
display = {}
for x in range(1, 101):
    display.setdefault(x, '*')
    if x % 3 == 0:
        display[x] = 'Crackle'
    if x % 5 == 0:
        display[x] = 'Pop'
    if x % 3 == 0 and x % 5 == 0:
        display[x] = 'CracklePop'
pprint.pprint(display)
