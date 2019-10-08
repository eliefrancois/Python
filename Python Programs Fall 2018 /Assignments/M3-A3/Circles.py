c1Y = int(input('enter circle 1 y value: ')) 
c1X = int(input('enter circle 1 x value: ')) 
c1R = int(input('enter radius for circle 1: ')) 
c2X = int(input('enter circle 2 x value: '))
c2Y = int(input('enter circle 2 y value: '))
c2R = int(input('enter radius for circle 2: '))
import math
dis = (c2X - c1X)^2 + (c2Y - c1Y)^2
rad = (c1R + c2R) * (c1R + c2R)

if dis == rad:
    print ('The circles intersect')
if dis > rad:
    print ('The circle is completely outside')
if dis < rad:
    print ('The circle is overlapping')
