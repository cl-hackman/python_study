import random

try:
    heads = 0
    tails = 0
    streak = 0
    lister = []
    for i in range(10001):
        for i in range(101):
            i = random.randint(0,1)
            if i == 0:
                heads = heads + 1
                lister.append('H')
            if i == 1:
                tails = tails + 1
                lister.append('T')  
            for i in range(len(lister)):
                if tails == 6 or heads == 6:
                    streak += 1
            break
except:
    pass
print(lister)
print(f'Chances: {heads} heads and {tails} tails')           
print('Probability: %s%% streak' %(streak/100))
 
