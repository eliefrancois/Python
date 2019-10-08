class radio:

    station = 1
    volume = 1 
       
    def __init__(self,station,volume):
        self.station = station
        self.volume = volume
        self.radio = False
    def getStation(self):
        return self.station
    def getVolume(self):
        return self.volume
    def turnOn(self):
        self.radio = True
    def turnOff(self):
        self.radio = False
    def stationUp(self):
        if self.radio == True:
            self.station += 1
        return self.station 
    def stationDown(self):
        if self.radio == True:
            self.station -= 1
        return self.station
    def volumeUp(self):
        if self.radio == True:
            self.volume += 1
        return self.volume 
    def volumeDown(self):
        if self.radio == True:
            self.volume -= 1
        return self.volume
    def __str__(self):
        if self.radio == True:
            return 'The radio station is ' + str(self.station) + ' and the volume is '  + str(self.volume)
        else:
            return 'The radio is off'



