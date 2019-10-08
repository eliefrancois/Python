def reverse(num):
    r = num % 10
    rev = str(r) 
    num = num/10
    while num > 0:
        r = int(num % 10)
        rev = rev + str(r) 
        num = num//10
    print(rev) 
    return int(rev)
def isPalindrome(num):
    if num == reverse(num):
        return True
    else:
        return False 
def main():
    num = int(input('enter number here: '))
    p = isPalindrome(num)
    
    if p==True :
        print('This is a Palindrome')
    else:
        print('This is not a Palindrome')

main()

