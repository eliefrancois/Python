num1 = int(input('Enter Number: '))
num2 = int(input('Enter Number: '))
num3 = int(input('Enter Number: '))
num4 = int(input('Enter Number: '))
avgNum = (num1 + num2 + num3 + num4)/4

if num1 > num2 and num1 > num3 and num1 > num4:
    print ('Highest number is', (num1))
if num2 > num1 and num2 > num3 and num2 > num4:
    print ('Highest number is', (num2))
if num3 > num1 and num3 > num2 and num3 > num4:
    print ('Highest number is', (num3))
if num4 > num1 and num4 > num2 and num4 > num3:
    print ('Highest number is', (num4))

if num1 < num2 and num1 < num3 and num1 < num4:
    print ('Lowest number is', (num1))
if num2 < num1 and num2 < num3 and num2 < num4:
    print ('Lowest number is', (num2))
if num3 < num1 and num3 < num2 and num3 < num4:
    print ('Lowest number is', (num3))
if num4 < num1 and num4 < num2 and num4 < num3:
    print ('Lowest number is', (num4))

print ('You entered: ', (num1,num2,num3,num4,))
print ('Average number is: ', (avgNum))


