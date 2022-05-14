import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    resultList = []
    for i in range(100):
        result = random.randint(0,1)
        resultList.append(result)

    counterzero = 0
    counterone = 0
    for res in resultList:
        if res == 0:
            counterzero+=1
        elif res == 1:
            counterone+=1

        if counterzero == 6 or counterone == 6:
            counterzero = 0
            counterone = 0
            numberOfStreaks+=1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))