annualIncome = int(input('Enter Annual Income Here: '))

if annualIncome <= 50000:
    taxRate = .05
    netIncome = annualIncome * taxRate
    print ('Your annual income is', annualIncome)
    print ('Your Tax bracket is', taxRate)
    print ('Your tax due  is', netIncome)
if annualIncome > 50000 and  annualIncome <= 200000:
    taxRate = .10
    netIncome = annualIncome * taxRate
    print ('Your annual income is', annualIncome)
    print ('Your Tax bracket is', taxRate)
    print ('Your tax due is', netIncome)
if annualIncome > 200000 and annualIncome <= 400000:
    taxRate = .15
    netIncome = annualIncome * taxRate
    print ('Your annual income is', annualIncome)
    print ('Your Tax bracket is', taxRate)
    print ('Your tax due  is', netIncome)
if annualIncome > 400000 and annualIncome <= 900000:
    taxRate = .25
    netIncome = annualIncome * taxRate
    print ('Your annual income is', annualIncome)
    print ('Your Tax bracket is', taxRate)
    print ('Your tax due is', netIncome)
if annualIncome > 900000:
    taxRate = .35
    netIncome = annualIncome * taxRate
    print ('Your annual income is', annualIncome)
    print ('Your Tax bracket is', taxRate)
    print ('Your tax due is', netIncome)
