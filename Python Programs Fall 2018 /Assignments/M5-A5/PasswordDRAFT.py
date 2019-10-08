def checkPassword(pw):
    if int(pw) > 3 and int(pw) < 10:
        print ('Valid password')
    else:
        print('Invalid password')
    return checkPassword 
def main():
    pw = str(input('Enter password here: '))
    if int(pw) > 3 and int(pw) < 10:
        print ('Valid password')
    else:
        print('Invalid password')


main()
    
