hours = float(input(' Enter amount of hours worked: '))
rate = float(input(' Enter rate here: '))
if hours <= 40:
    gross = rate * hours
elif hours > 40:
    overTime = hours - 40
    overRate = rate * 1.5
    gross = rate * 40 + overTime * overRate
    
print (gross)
