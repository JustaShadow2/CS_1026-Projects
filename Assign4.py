from Flight import *
from Airport import *

#airportFile = "airports.txt"
#flightFile = "flights.txt"

allAirports = []
listWithFlights = []
listWithAirports = [] #data still has spaces which needs to be dealt with. afterwards, will be stored in allAirports
allFlights = {}

def loadData(airportFile, flightFile):
    try:
        airportFileTest = open(airportFile, "r")
        flightFileTest = open(flightFile, "r")
        #close the files
        airportFileTest.close()
        flightFileTest.close()
    except FileNotFoundError:
        #exit the program
        return False

    with open(airportFile, "r") as f:
        for line in f:
            contentStrip = line.lstrip("")
            contentStrip = contentStrip.rstrip()
            contentStrip = contentStrip.lstrip()
            contentStrip = contentStrip.rstrip()
            contentStrip = contentStrip.split(",")
            listWithAirports.append(contentStrip)

        for row in listWithAirports:
            for i in range(len(row)):
                row[i] = row[i].strip(" ")
                row[i] = row[i].strip("\t")
            allAirports.append(Airport(row[0], row[2], row[1]))
        #print(allAirports)

    with open(flightFile, "r") as f:
        for line in f:
            contentStrip1 = line.lstrip("")
            contentStrip1 = contentStrip1.rstrip()
            contentStrip1 = contentStrip1.lstrip()
            contentStrip1 = contentStrip1.rstrip()
            contentStrip1 = contentStrip1.split(",")
            listWithFlights.append(contentStrip1)

        for row in listWithFlights:
            for i in range(len(row)):
                row[i] = row[i].strip(" ")
                row[i] = row[i].strip("\t")
            # check if key already exists in dictionary
                
            if row[1] in allFlights.keys():
                # if key exists, add a new object to the dictionary
                # find the airport object that matches the code of row[1] and row[2]
                code = row[0]
                origAirport = getAirportByCode(row[1])
                destAirport = getAirportByCode(row[2])
                allFlights[row[1]].append(Flight(code, origAirport, destAirport))
                #allFlights[row[1]].append(list([row[0], row[1], row[2]]))
            else:
                code = row[0]
                origAirport = getAirportByCode(row[1])
                destAirport = getAirportByCode(row[2])
                # if key does not exist, create a new key-value pair with the value as a flight object
                allFlights[row[1]] = [Flight(code, origAirport, destAirport)]
                #allFlights[row[1]] = list([list([row[0], row[1], row[2]])])
    return (allAirports, allFlights)

def getAirportByCode(code):
    #check each airport in allAirports to see if the code matches the code given
    for i in range(len(allAirports)):
        if allAirports[i].getCode() == code:
            return allAirports[i]
    return -1

def findAllCityFlights(city):
    #return a list of all flights that have the given city as either the origin or destination
    for i in range(len(allAirports)):
        if city == allAirports[i].getCity():
            #find all flights that have allAirports[i].getCode() as the key in allFlights
            code = allAirports[i].getCode()
    cityFlights = []
    #iterate through each key in allFlights
    for key in allFlights.keys():
        #iterate through each flight in the list of flights
        for i in range(len(allFlights[key])):
            #check if the flight's origin airport code matches the given airport code
            if allFlights[key][i].getDestination().getCode() == code:
                cityFlights.append(allFlights[key][i])
            if allFlights[key][i].getOrigin().getCode() == code:
                cityFlights.append(allFlights[key][i])
    return cityFlights  

def findAllCountryFlights(country):
    #return a list of all flights that have the given country as either the origin or destination
    codes = []
    for i in range(len(allAirports)):
        if country == allAirports[i].getCountry():
            codes.append(allAirports[i].getCode())
            
    countryFlights = []
    #iterate through each key in allFlights
    for key in allFlights.keys():
        #iterate through each flight in the list of flights
        for i in range(len(allFlights[key])):
            #check if the flight's origin airport code matches the given airport code
            if allFlights[key][i].getDestination().getCode() in codes: #check if the destination is in the list of codes
                countryFlights.append(allFlights[key][i])
            if allFlights[key][i].getOrigin().getCode() in codes:
                countryFlights.append(allFlights[key][i])
    return countryFlights

def findFlightBetween(origAirport, destAirport):
    #direct flight between two airports
    if origAirport.getCode() in allFlights.keys():
        for i in range(len(allFlights[origAirport.getCode()])):
            if allFlights[origAirport.getCode()][i].getDestination() == destAirport:
                #return allFlights[origAirport.getCode()][i]
                return "Direct Flight: " + origAirport.getCode() + " to " + destAirport.getCode()
                #if no direct flight, else statement will be executed

            #find a double flight between two airports
        connectionAirport = set()   
        if origAirport.getCode() in allFlights.keys():
            for i in range(len(allFlights[origAirport.getCode()])):
                #check if any of those flights have a destination that is the origin of another flight
                if allFlights[origAirport.getCode()][i].getDestination().getCode() in allFlights.keys():
                    for j in range(len(allFlights[allFlights[origAirport.getCode()][i].getDestination().getCode()])):
                        if allFlights[allFlights[origAirport.getCode()][i].getDestination().getCode()][j].getDestination() == destAirport:
                            #print([allFlights[origAirport.getCode()][i], allFlights[allFlights[origAirport.getCode()][i].getDestination().getCode()][j]])
                            #return a set of all the connecting airports
                            connectionAirport.add(allFlights[origAirport.getCode()][i].getDestination().getCode())
                            #if connectionAirport is not empty, return the set. else, return -1
        if len(connectionAirport) > 0:
            return connectionAirport
        else:
            return -1
    return -1

def findReturnFlight(firstFlight):
    #given a flight from A to B, find a flight from B to A
    #check if the destination of the first flight is in allFlights
    if firstFlight.getDestination().getCode() in allFlights.keys():
        for i in range(len(allFlights[firstFlight.getDestination().getCode()])):
            if allFlights[firstFlight.getDestination().getCode()][i].getDestination() == firstFlight.getOrigin():
                return allFlights[firstFlight.getDestination().getCode()][i]
    return -1


