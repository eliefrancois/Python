import random
def main():
    wHours=[] #An empty list of array
    for i in range(3):
        Hours=[] #An empty list for storing employee weekly hours
        for j in range(7):
            Hours.append(random.randint(1,10))
            wHours.append(Hours) 
            print(" Mon Tue Wed Thu Fri Sat Sun")
            for i in range(3):
                print("Employee-",i+1,end ="")
                for j in range(7):
                    print(" ",wHours[i][j],end =" ")
                    print("\n")
                    addHours(wHours)  
  
def addHours(wHours):
    print("Employee Weekly Hours")
for i in range(3):
    print(sum(wHours[i]),i+1,' ')

main()

