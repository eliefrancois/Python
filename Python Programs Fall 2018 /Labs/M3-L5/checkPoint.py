x = int(input('Enter x coordinate: '))
y =int(input('Enter y coordinate: '))

print('x coordinate is', x)
print('y coordinate is', y)

if x > 0 and y > 0:
  print (x,y,'is in the First quadrant')
  
elif x < 0 and y > 0:
  print (x,y,'is in the Second quadrant')
  
elif x < 0 and y < 0:
  print (x,y,'is in the Third quadrant')

elif x > 0 and y < 0:
  print (x,y,'is in the Fourth quadrant')

elif x == 0 and (y > 0) or (y < 0):
  print (x,y,'is on the y axis')

elif (x > 0) or (x < 0) and y == 0:
  print (x,y,'is on the x axis')

elif x == 0 and y == 0:
  print ("(" + str(x) + "," + str(y) + ') is at the origin')
