from Airport import *

class Flight:

    def __init__(self, flightNo, origin, destination):
        if not isinstance(origin, Airport) or not isinstance(destination, Airport):
            raise TypeError("The origin and destination must be Airport objects")
        self._flightNo = flightNo
        self._origin = origin
        self._destination = destination

    #return the flight number, origin, destination, and if it is domestic or not
    def __repr__(self):
        if self.isDomesticFlight():
            return "Flight: " + self._flightNo + " from " + self._origin.getCity() + " to " + self._destination.getCity() + " {domestic}"
        else:
            return "Flight: " + self._flightNo + " from " + self._origin.getCity() + " to " + self._destination.getCity() + " {international}"

        

    def __eq__(self, other):
        if not isinstance(other, Flight):
            #raise TypeError("The other object must be a Flight object") # does not ask for typeerror?
            return False
        return self._origin == other._origin and self._destination == other._destination

    def getFlightNumber(self):
        return self._flightNo

    def getOrigin(self):
        #return the origin 
        return self._origin 

    def getDestination(self):
        return self._destination

    def isDomesticFlight(self):
        return self._origin.getCountry() == self._destination.getCountry()

    def setOrigin(self, origin):
        self._origin = origin

    def setDestination(self, destination):
        self._destination = destination
