def printChrs(chr1,chr2):
    lines = 0
    while ord(chr1) <= ord(chr2):
        if lines == 5:
            print()
            print (str(chr1) + " ", end = "")
            lines = 1
        else:
            print (str(chr1) + " ", end = "")
            lines+=1
        chr1 = chr(ord(chr1) + 1)
def main():
    chr1 = input('Enter start character:  ')
    chr2 = input('Enter end character: ')
    if (ord(chr1) < ord(chr2)):
        printChrs(chr1,chr2)
    else:
        print('first letter should come before the second')
        chr1 = chr(input('Enter start character:  '))
        chr2 = chr(input('Enter end character: '))
        printChrs(chr1,chr2)
        
        
main()       
