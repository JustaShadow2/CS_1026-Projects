#Arjun Atwal
#251313474
#Assignment 3
#CS 1026A

import csv
def getInformation(selectedCountry,rankingFileName,capitalsFileName): #defined in assignment instructions
    try:
        outfile = open("output.txt", 'w', encoding='utf8')
    except FileNotFoundError:
        print("File not found")
        return


    #1 count total number of univeristies in the ranking file
    with open(rankingFileName) as f: #open the file
        reader = csv.reader(f) #read the file
        data = list(reader) #store the file in a list
        totalUni = len(data)-1 #minus 1 because the first row is the header
        outfile.write("Total number of universities => "+str(totalUni)+"\n")

    #2 print all available countries from the ranking file
    with open(rankingFileName) as f:
        reader = csv.reader(f)
        data = list(reader)
        countriesList = []
        for row in data:
            if row[2].upper() not in countriesList:
                countriesList.append(row[2].upper())
        countriesList = countriesList[1:] #remove the header
        outfile.write("Available countries => "+str(countriesList)+"\n")        

    #3 print all available continents in the order of countries
    possibleContinents = ["AFRICA","ASIA","EUROPE","NORTH AMERICA","SOUTH AMERICA","AUSTRALIA", "OCEANIA"] #list of possible continents. included to ensure false values such as antarctica (there are no countries and no universities) and central america do not impact the data. This can be changed to allow different values if not needed
    with open(capitalsFileName) as f: 
        reader = csv.reader(f)
        data = list(reader)
        continentsList = []
        for i in range (len(countriesList)): #loop through the countries list
            for row in data: #loop through the capitals file
                if row[0].upper() == countriesList[i]: #if the country in the capitals file matches the country in the countries list
                    if row[5].upper() not in continentsList: #if the continent is not already in the list
                        if row[5].upper() in possibleContinents: #if the continent is in the possible continents list
                            continentsList.append(row[5].upper())
        outfile.write("Available continents => "+str(continentsList)+"\n")

    #4 print the international rank and university that holds that rank of the selected country
    with open(rankingFileName) as f:
        reader = csv.reader(f)
        data = list(reader)
        for row in data:
            if row[2].upper() == selectedCountry.upper(): #if the country is the selected country
                worldRank = row[0] 
                outfile.write("At international rank => "+str(worldRank)+" the university name is => "+row[1].upper()+"\n")
                break
    
    #5 find the university with the highest national rank of the selected country
    with open(rankingFileName) as f:
        reader = csv.reader(f)
        data = list(reader)
        highestRank = 1 #set the highest rank to 1
        for row in data:
            if row[2].upper() == selectedCountry.upper(): 
                if int(row[3]) == highestRank: #if the rank is the same as the highest rank
                    highestRank = int(row[3]) #set the highest rank to the current rank
                    uniName = row[1] 
        outfile.write("At national rank => "+str(highestRank).upper()+" the university name is => "+str(uniName).upper()+"\n")

    #6 find the average score of the selected country
    with open(rankingFileName) as f:
        reader = csv.reader(f)
        data = list(reader)
        totalScore = 0
        count = 0
        for row in data:
            if row[2].upper() == selectedCountry.upper():
                totalScore += float(row[8]) #add the score to the total score
                count += 1 #add 1 to the count
        averageScore = totalScore/count #calculate the average score
        outfile.write("The average score is => "+str(averageScore)+"%\n")  

    #7 find the continent of the selected country
    countries = [] #initialize everything
    continent = ''
    scoreList = []
    highestScore = 0.0
    
    with open(capitalsFileName) as f:
        reader = csv.reader(f)
        data = list(reader)
        for row in data:
            if row[0].upper() == selectedCountry.upper(): 
                continent = row[5] #set the continent to the continent of the selected country

    #7 find all countries in the same continent as the selected country (this could be combined with the code above, but seperating the tasks made it easier to code and makes it easier to read)
    with open(capitalsFileName) as f:
        reader = csv.reader(f)
        data = list(reader)
        for row in data:
            if row[5].upper() == continent.upper():
                countries.append(row[0]) #add the country to the list
                
    #7 find the the highest score of the countries in the same continent as the selected country
    with open(rankingFileName) as f:
        reader = csv.reader(f)
        data = list(reader)
        for row in data:
            if row[2] in countries:
                scoreList.append(float(row[8])) #add the score to the list
        highestScore = (max(scoreList, default=1.0)) #set the highest score to the highest score in the list
        #outfile.write("The highest score in the continent is => "+str(highestScore)+"%\n")

    #7 find the relative score of the selected country by taking the average/highest score
    relativeScore = (averageScore/highestScore)*100 
    outfile.write("The relative score to the top university in {} is => ({:.2f} / {:.2f}) x 100% = {:.2f}%\n".format(continent.upper(),averageScore,highestScore,relativeScore)) #rounded for 2 decimal places only for the print statement

    #8 find the capital of the selected country
    with open(capitalsFileName) as f:
        capitalCity = ''
        reader = csv.reader(f)
        data = list(reader)
        for row in data:
            if row[0].upper() == selectedCountry.upper():
                capitalCity = row[1].upper() #set the capital city to the capital city of the selected country
                outfile.write("The capital is => "+str(capitalCity)+"\n") 


    #9 check if a university has the capital city in its name
    with open(rankingFileName) as f:
        count = 0
        reader = csv.reader(f)
        data = list(reader)
        for row in data:
            if capitalCity.upper() in row[1].upper(): #if the capital city is in the university name
                count += 1
                outfile.write('#'+str(count)+" The university with the capital city in its name is => "+row[1].upper()+"\n")