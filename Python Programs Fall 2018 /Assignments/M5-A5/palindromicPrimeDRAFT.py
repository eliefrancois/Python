def reverse(num):
    r = num % 10
    rev = str(r) 
    num = num/10
    while num > 0:
        r = int(num % 10)
        rev = rev + str(r) 
        num = num//10
    print('Reverse?:',rev) 
    return int(rev)
def isPalindrome(num):
    if num == reverse(num):
        return True
    else:
        return False 
def isPrime(num):
    if num <= 1:
        return false
    for x in range(2,num):
        if not num % x:
            return False
    return True 
def main():
    num = int(input('Enter number here: '))
    print('Palindrome?:',isPalindrome(num))
    print('Prime?:',isPrime(num))
main()
    
