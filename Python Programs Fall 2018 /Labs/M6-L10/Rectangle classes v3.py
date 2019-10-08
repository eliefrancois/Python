class Rectangle:
    def __init__(self,l=1,w=1):
        self.l = l
        self.w = w
        self.a = (l*w)
        self.p = 2*(l+w) 
    

rec1 = Rectangle() # this creates the object with the values entered
rec2 = Rectangle(5,6)
def getArea():
    return self.a
def getPerimeter():
    return self.p
def getLength():
    return self.l
def getWidth():
    return self.w
def main():
    print('First object:')
    print('\t','Length:',rec1.l) # this prints rec1's length
    print('\t','Width:',rec1.w) # this prints rec1's width
    print('\t','Area:',rec1.a) # this prints rec1's area
    print('\t','Perimeter:',rec1.p) # this prints rec1's perimeter
    print()
    print('Second object:')
    print('\t','Length:',rec2.l)
    print('\t','Width:',rec2.w)
    print('\t','Area:',rec2.a)
    print('\t','Perimeter:',rec2.p)

main()








        #print(Rectangle.__init__(self,5,6,5,6))

        
