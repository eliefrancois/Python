num = -1
max = num
count = 0
while num != 0:
    num = int(input('Enter number(0 to quit): '))
    if num > 0:
        print(num)
        if num > max:
            max = num
            count = 1
        elif max == num:
            count += 1
print ('Largest number',max)
print ('Occuracnes',count)
