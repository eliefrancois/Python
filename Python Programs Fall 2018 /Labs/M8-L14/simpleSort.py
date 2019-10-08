def bubbleSort(unsorted):
    for i in range(len(unsorted)):
        comp = 0
        for j in range((i+1),len(unsorted)):
            if unsorted[i] > unsorted[j]:
                temp = unsorted[i]
                unsorted[i] = unsorted[j]
                unsorted[j] = temp
                comp = comp + 1
    return comp 

myArray = [54,26,93,17,77,31,44,55,20]
bubbleSort(myArray)
print(myArray)
comp = bubbleSort(myArray)
print('Bubble sorted values:', myArray)
print('Bubble sort swaps:', comp)



def selectionSort(unsorted):
    comp = 0 
    for i in range(len(unsorted)):
        positionOfMin=i
        for j in range(i+1,len(unsorted)):
            if unsorted[positionOfMin]>unsorted[j]:
                positionOfMin = j
        if positionOfMin != i:
            temp = unsorted[i]
            unsorted[i] = unsorted[positionOfMin]
            unsorted[positionOfMin] = temp
            comp = comp + 1
    return comp 

myArray = [54,26,93,17,77,31,44,55,20]
selectionSort(myArray)
print(myArray)
comp = selectionSort(myArray)
print('Selection sorted values:', myArray)
print('Selection sort swaps:', comp)




def insertionSort(unsorted):
    comp = 0
    for index in range(1,len(unsorted)):
        currentvalue = unsorted[index]
        position = index

        while position>0 and unsorted[position-1]>currentvalue:
            unsorted[position]=unsorted[position-1]
            position = position-1
            comp = comp +1 

        unsorted[position]=currentvalue
    return comp

myArray = [54,26,93,17,77,31,44,55,20]
insertionSort(myArray)
print(myArray)
comp = insertionSort(myArray)
print('Insertion sorted values:', myArray)
print('Insertion sort swaps:', comp)


