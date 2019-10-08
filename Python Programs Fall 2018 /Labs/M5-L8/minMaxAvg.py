def max(x,y,z):
    if x > y and x > z:
        max = x
    elif y > x and y > z:
        max = y
    else:
        max = z
    return max 
def min(x,y,z):
    if x < y and x < z:
        min = x
    elif y < x and y < z:
        min = y
    else:
        min = z
    return min 
def avg(x,y,z):
    avg = (x + y + z)/3
    return avg 
def main():
    x = int(input('Enter number here: '))
    y = int(input('Enter Number here: '))
    z = int(input('Enter number here: '))
    print('You entered',x,y,z)
    print('Max number is',max(x,y,z))
    print('Min number is',min(x,y,z))
    print('Average number is',avg(x,y,z))

main()
