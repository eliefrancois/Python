h = int(input('Enter height here in inches: '))
w = int(input('Enter weight here in pounds: '))
a = int(input('Enter age here: '))
g = input('Enter gender here M or F: ').upper()
e = 0
if g == 'M':
    bMR = 66+(6.23*w)+(12.7*h)-(6.8*a)
    print('Your BMR is',bMR)
    e = int(input('Enter level of exercise from 1-5: '))
if g == 'F':
    bMR = 655+(4.35*w)+(4.7*h)-(4.7*a)
    print('Your BMR is',bMR)
    e = int(input('Enter level of exercise from 1-5: '))
if e == 1:
    dCA = (bMR*1.2)
    print('Your DCA',dCA)
elif e == 2:
    dCA = (bMR*1.375)
    print('Your DCA',dCA)
elif e == 3:
    dCA = (bMR*1.55)
    print('Your DCA',dCA)
elif e == 4:
    dCA = (bMR*1.725)
    print('Your DCA',dCA)
elif e == 5:
    dCA = (bMR*1.9)
    print('Your DCA',dCA)


