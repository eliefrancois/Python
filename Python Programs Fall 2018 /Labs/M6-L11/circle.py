import math
class circle:

    radius = 1
    def __init__(self,radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def setRadius(self,radius):
        self.radius = radius 
    def getArea(self):
        return math.pi * self.radius**2
    def getPerimeter(self):
        return math.pi * (self.radius)*2
    def __str__(self):
       return 'The radius is ' + str(self.radius)
