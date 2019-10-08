import math 
def __init__(self,a,b,c,disc):
        self.a = a
        self.b = b
        self.c = c
        self.disc = disc

class quadraticEquation(a,b,c):
    def getDiscriminant(self,a,b,c):
        disc = (b**2)-(4*a*c)
        return disc
    def getRoot1(self,a,b):
        r1 = (-b +  math.sqrt(disc) ) / 2*a
        return r1
    def getRoot2(self,a,b):
        r2 = (-b - math.sqrt(disc) ) / 2*a
        return r2

r1 = quadraticEquation(3,8,4)
print(r1.getDiscriminant(3,8,4))
print(r1.getRoot1(3,8))

