def isValid(l,w):
    if w + l >= 30:
        print('Is valid')
    else:
        print('Not valid')
        return isValid
def Area(l,w):
    Area = (l * w)
    return Area
def Perimeter(l,w):
    Perimeter = 2*(l+w)
    return Perimeter
def testMyRectangle():
        w = float(input('Enter width here: '))
        l = float(input('Enter length here: '))
        print('Entered width:',w)
        print('Entered length:',l)
        print('Area:',Area(l,w))
        print('Perimeter:',Perimeter(l,w))
        print(isValid(l,w))
        
    



testMyRectangle()
