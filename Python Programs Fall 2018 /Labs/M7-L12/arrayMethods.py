arraySize = 5 
ogArry = []
import random # to make random num
import math

for i in range (0,arraySize):
    randNum = random.randint(1,101) # generates random number between 1-100
    ogArry.append(randNum)
print('Original array:',end = ' ') # makes next print line stay on same line 
print(*ogArry, sep = ',') # separates inputs with comma
    
    
    
def arrayMax():
    print('Max value:',max(ogArry))

def arrayMin():
    print('Min value:',min(ogArry))

def arraySquared(ogArry):
    squared = []
    for i in ogArry:
        squared.append(i**2)
    return print('Squared array:',squared) #idk how to take away [] around numbers 
def arrayRev():
    rev = ogArry[::-1] #idk how to take away [] around numbers
    print('Reversed array:',rev)

arrayMax()
arrayMin()
arraySquared(ogArry)
arrayRev()
