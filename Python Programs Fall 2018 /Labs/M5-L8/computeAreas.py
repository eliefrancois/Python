import math 

def sqArea(s):
    sqArea = pow(s,2)
    return sqArea

def recArea(w,l):
    recArea = (w * l)
    return recArea 

def cirArea(r):
    cirArea = math.pi*pow(r,2)
    return cirArea

def triArea(b,h):
    triArea = (.5*b)*h
    return triArea
def main():
    s = float(input('Enter Square side: '))
    w = float(input('Enter Rectangle width: '))
    l = float(input('Enter Rectangle length: '))
    r = float(input('Enter Circle radius: '))
    b = float(input('Enter Triangle base: '))
    h = float(input('Enter Triangle height: '))
    print('Square side:',s)
    print('Square area:',sqArea(s))
    print('Rectangle width:',w)
    print('Rectangle length:',l)
    print('Rectangle area:',recArea(w,l))
    print('Circle radius:',r)
    print('Circle area:', cirArea(r))
    print('Triangle base:',b)
    print('Triangle height:',h)
    print('Triangle area:',triArea(b,h))

main()
