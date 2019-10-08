Rows = int(input('enter rows: '))
Cols = int(input('enter columns: '))
sym = input('enter symbol here: ')

for i in range(Rows):
    print(sym, end='')
    for j in range(Cols-1):
        i*=j
        print(sym, end='')
    print('')
