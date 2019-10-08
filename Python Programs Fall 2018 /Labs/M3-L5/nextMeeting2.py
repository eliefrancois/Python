todaysDate = int(input('Enter an interger for current day of the week from 0 - 6, Sunday is 0 and Saturday is 6: '))

if todaysDate == 0:    
    print ('Today is Sunday')
elif todaysDate == 1:
    print ('Today is Monday')
elif todaysDate == 2:
    print ('Today is Tuesday')
elif todaysDate == 3:
    print ('Today is Wednesday')
elif todaysDate == 4:
    print ('Today is Thursday')
elif todaysDate == 5:
    print ('Today is Friday')
elif todaysDate == 6:
    print ('Today is Saturday')

daysElapsed = int(input('Enter the number of days elapsed since today: '))
nextMeeting = ((daysElapsed+todaysDate) % 7)

if nextMeeting == 0:
    print ('The next meeting is Sunday')
if nextMeeting == 1:
    print ('The next meeting is Monday')
if nextMeeting == 2:
    print ('The next meeting is Tuesday')
if nextMeeting == 3:
    print ('The next meeting is Wendesday')
if nextMeeting == 4:
    print ('The next meeting is Thursday')
if nextMeeting == 5:
    print ('The next meeting is Friday')
if nextMeeting == 6:
    print ('The next meeting is Saturday')
        



