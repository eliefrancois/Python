def minMaxAvg(mymath): #function to calculate min, max, avg
    print("Highest grade is: ",max(max(x) for x in mymat)) #recursively calling max over matrix
    print("Lowest grafe is: ",min(min(x) for x in mymat)) #recursively calling min over matrix
    sum = 0;
for i in range(4):
    for j in range(4):
        sum += mymath[i][j]; #summing up matrix elements
        print("Average is: ",sum/16) #this gives the average
        from random import randint
        mymath = [[ randint(0,100) for x in range(0,4)] for y in range(0,4)] #genarates random array of numbers
        print("Populatedd matrix is: ")

for i in mymat:
    print(i)

minMaxAvg(mymat)
