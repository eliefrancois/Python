def sumDigits(num):
    sum = 0
    lastDigit = 0
    while num > 0:
        lastDigit = num % 10
        sum += lastDigit
        num = int(num/10)
    return sum 
        
        
    return sumDigits
def main():
    num = int(input('Enter number: '))
    print('You entered', num)
    print('Sum of digits',sumDigits(num))
main()
