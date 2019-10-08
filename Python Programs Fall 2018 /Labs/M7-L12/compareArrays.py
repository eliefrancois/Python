arraySize = 0
arraySize = int(input('Input array size: '))
arry1 = []
arry2 = []
for i in range (0,arraySize):
    arry1Num = int(input('Input first array: '))
    arry1.append(arry1Num)
for j in range (0,arraySize):
    arry2Num = int(input('Input second array: '))
    arry2.append(arry2Num)
print('Array size:',arraySize)
print('First array:', end = ' ')
print( *arry1, sep = ',')
print('Second array:', end = ' ')
print( *arry2, sep = ',')
print('Judgment:',end = ' ')

def compare(arry1,arry2):
    if arry1 == arry2:
        print('The arrays are identical')
    else:
        print('The arrays are not identical')
    
    
compare(arry1,arry2)
