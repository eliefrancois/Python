def findIndex(l):
    k=max(l)
    return l.index(k)
li=[]#Input List
print('Enter ten numbers: ')
for i in range(10):
    li.append(int(input()))
print('The Index of the first largest value in the array is: ',findIndex(li))

