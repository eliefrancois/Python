import datetime
import calendar
class bankAccount:
  
   _id = 0
   _balance = 0.0
   _annualInterestRate = 0.0
   _dateCreated = datetime.datetime.now()

   def __init__(self):
       self._id = 0
       self._balance = 0.0
       self._annualInterestRate = 0.0
       self._dateCreated = datetime.today()
   def __init__(self , id , balance , annualInterestRate , dateCreated):
       self._id = id
       self._balance = balance
       self._annualInterestRate = annualInterestRate
       self._dateCreated = dateCreated

   def getId(self):
       return self._id

   def getBalance(self):
       return self._balance

   def getAnnualInterestRate(self):
       return self._annualInterestRate

   def getDateCreated(self):
       return self._dateCreated

   def setId(self , id):
       self._id = id

   def setBalance(self , balance):
       self._balance = balance

   def setAnnualInterestRate(self , annualInterestRate):
       self._annualInterestRate = annualInterestRate


   def getMonthlyInterestRate(self):
       return self._annualInterestRate/12.0

   def getMonthlyInterest(self):
       return self._balance * self.getMonthlyInterestRate()

   def withdraw(self , amount):
       self._balance -= amount

   def deposit(self , amount):
       self._balance += amount

   def toString(self):
       print("Account ID:\t\t" + str(self._id))
       print("Account Balance:\t$" + str(self._balance))
       print("Interest Rate:\t\t" + str(self._annualInterestRate) + "%")
       print(self._dateCreated.strftime("%a %b %d %H:%M:%S %Y"))
