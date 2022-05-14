for x in range(101):
    x > 0
    print(x)
    if x % 3 == 0:
        print(f'{x}: Crackle ')
    if x % 5 == 0:
        print(f'{x}: Pop')
    if x % 3 == 0 and x % 5 == 0:
        print(f'{x}: CrackelePop')
