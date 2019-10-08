accNum = int(input(' Enter Account Number Here: '))
serType = input(' What service type do you have? R or P?: ').upper()
if serType == 'R':
    amountDue = 15          
    minutesUsed = int(input('Enter the number of minutes used: '))
    if (minutesUsed-50) > 0:
        amountDue = (minutesUsed-50 )*.5 + amountDue
        
elif serType == 'P':
    amountDue = 25
    dayMinutes = int(input(' Enter the number of day minutes used: '))
    nightMinutes = int(input(' Enter the number night minutes used: '))
    if (dayMinutes-100) > 0:
        amountDue += .20 * (dayMinutes - 100)
    if (nightMinutes - 100) > 0:
        amountDue += .10 * (nightMinutes - 100)

print (' Your account number is ' + str(accNum))
    
if serType == 'R':
    print (' Number of minutes used, ' +  str(minutesUsed))
    print (' Total Amount due, ' + str(amountDue))
elif serType == 'P':
    print (' Number of Day Minutes used,' + str(dayMinutes))
    print (' Number of Night Minutes used,' + str(nightMinutes))
    print (' Total Number of minutes used,' + str(dayMinutes + nightMinutes))
    print (' Total Amount Due,' + str(amountDue))
    
