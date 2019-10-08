num1 = 2
num2 = int(input('Enter number here: '))
while num2 < 20 or num2 > 60:
    num2 = int(input('Incorrect value try again: '))
    
sumEven = 0
while num1 <= num2:
    sumEven = sumEven+num1
    num1+=2

print('Entered value :', num2)
print('Sum of even numbers between 2 and',num2,':',sumEven)
    
