import bankAccount
import datetime

myObject = bankAccount.bankAccount(123456,10000,2.5,datetime.datetime.today())
myObject.withdraw(3500)
myObject.deposit(500)
print(myObject.getBalance())
print(myObject.getMonthlyInterest())
print(myObject.getDateCreated().strftime("%a %b %d %H:%M:%S %Z %Y"))

