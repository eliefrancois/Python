Q = int(input(' Enter number of Quarters: '))
D = int(input(' Enter number of Dimes: '))
N = int(input(' Enter number of Nickels: '))
P = int(input(' Enter number of Pennies: ')) 
totalCents = Q * 25 + D * 10 + N * 5 + P
dollars  = totalCents//100
remCent = totalCents%100
print (' You entered ',Q,' Quarters ')
print (' You entered ',D,' Dimes ')
print (' You entered ',N,' Nickels ')
print (' You entered ',P,' Pennies ')
print (' Your total is ',dollars,' dollars and ',remCent,' cents.')  
