smallWeight = float(input(' Enter small box weight: '))
smallPrice = float(input(' Enter small box price: '))
largeWeight = float(input(' Enter large box weight: '))
largePrice = float(input(' Enter large box price: '))
if smallWeight/smallPrice > largeWeight/largePrice:
    print ( 'The small box is a better deal')
elif smallWeight/smallPrice < largeWeight/largePrice:
    print ( 'The large box is a better deal')
