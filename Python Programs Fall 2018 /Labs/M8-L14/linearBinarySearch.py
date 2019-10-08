numberarry = []
target = int(input('What is your target?: '))
size= int(input('How many values would you like?: '))
for j in range (0,size):
    number = int(input('Enter number here: '))
    numberarry.append(number)

numberarry.sort()
print(numberarry)

def linearSearch(numberarry,target):
    i = 0
    comp = 1

    while i < len(numberarry):
        if numberarry[i] == target:
            return comp
        comp = comp + 1
        i = i + 1

    return -1

comp = linearSearch(numberarry,target)
if comp != -1:
    print('Number',target,'was found after',comp,'comparisons')

else:
    print('Number',target,'was not found!')



def binarySearch(numberarry, target):
    first = 0
    last = len(numberarry)-1
    found = False
    comp = 1 
	
    while first<=last and not found:
        midpoint = (first + last)//2
        if numberarry[midpoint] == target:
            found = True
            return comp
    
        else:
            if target < numberarry[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
        comp = comp + 1
    return -1
	
comp = binarySearch(numberarry, target)
if comp != -1:
    print('Number',target,' was found after',comp,'comparisons')

