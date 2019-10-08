class Stock:
    def __init__(self,name,sym,clP,cuP):
        self.name = name
        self.sym = sym
        self.clP = clP
        self.cuP = cuP
        self.CP = ((cuP-clP)/clP*100)

stk1 = Stock('Google','GOG',134.67,131.98)
stk2 = Stock('Microsoft','MSF',156.52,161.22)
def getname():
    return self.name 
def getsymbol():
    return self.sym
def setClosingPrice():
    return self.clP 
def setCurrentPrice():
    return self.cuP 
def getChangePercent():
    return self.CP
    
    
def main():
    print(stk1.name,'Stock:')
    print('\t','Symbol:''\t',stk1.sym)
    print('\t','Closing Price:''\t',stk1.clP)
    print('\t','Current Price:''\t',stk1.cuP)
    print('\t','Change Percent: '+ str(stk1.CP) + '%')
    print('\t',stk1.name,'stock closing price is $' +str(stk1.clP))
    print()
    print(stk2.name,'Stock:')
    print('\t','Symbol:''\t',stk2.sym)
    print('\t','Closing Price:''\t',stk2.clP)
    print('\t','Current Price:''\t',stk2.cuP)
    print('\t','Change Percent: ' + str(stk2.CP) + '%')
    print('\t',stk2.name,'stock closing price is $' + str(stk2.clP))
    
main()
