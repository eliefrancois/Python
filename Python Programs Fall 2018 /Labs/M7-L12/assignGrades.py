
clzSze = 0 
clsSze = int(input('Class size: '))
grde =[]
for i in range  (0,clsSze):
    indivGrde = int(input('Enter grade: '))
    if indivGrde >=0 and indivGrde <= 100:
        grde.append(indivGrde)
print('')
print('')
print('Class size: ',clsSze)

print('Entered grades:', end = ' ')
print( *grde, sep = ',')
print('')
print('')

for j in range(0,clsSze):
    if grde[j]>= 90 and grde[j] <= 100:
        print('Student', j , 'score is', grde[j], 'and grade is A')
    elif grde[j] >= 80 and grde[j] <=89:
        print('Student', j , 'score is', grde[j], 'and grade is B')
    elif grde[j] >= 70 and grde[j] <= 79:
        print('Student', j , 'score is', grde[j], 'and grade is C')
    elif grde[j] >= 60 and grde[j] <= 69:
        print('Student', j , 'score is', grde[j], 'and grade is D')
    elif grde[j] < 60:
        print('Student', j , 'score is', grde[j], 'and grade is F')
            
        
