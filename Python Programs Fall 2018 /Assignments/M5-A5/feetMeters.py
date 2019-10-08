def feetToMeter(f):
    feetToMeter = (f * .305)
    return feetToMeter
def meterToFeet(m):
    meterToFeet = (m * 3.279)
    return meterToFeet
def main():
    measure = input('Which measurement (m)eter or (f)eet?: ').upper()
    if measure == 'M':
        m = float(input('Enter meter here: '))
        print('Meter to feet is:',meterToFeet(m))
    elif measure == 'F':
        f = float(input('Enter feet here: '))
        print('Feet to meter is:',feetToMeter(f))
    else:
        print('incorrct measurement try again')
main()
