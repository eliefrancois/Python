val = int(input('Enter number between 1-100: '))
while val <= 0 or val > 100:
	val = int(input('Invaild number try again: '))
if val >= 1 and val <= 100:
	sum1 = (val*(val+1))/2
print('You entered:', val)
print('Sum of values:',sum1)
