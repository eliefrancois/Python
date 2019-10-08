row = 3
stars = 11
spaces = 0
for i in range(0,6):
    for j in range(0,spaces):
        print(' ', end = '')
    for e in range(stars,0,-1):
        print('*', end = '')
    print()
    stars = stars-2
    spaces = spaces+1

stars = 3
spaces = 4
row = 5
for k in range(0,5):
    for y in range(spaces,0,-1):
        print(' ', end = '')
    for z in range(0,stars):
        print('*', end = '')
    print()
    stars = stars + 2
    spaces = spaces-1 
        
        
