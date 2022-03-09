from GetPath import getRandomPath
from GetPathDistance import getPathDistance
import numpy as np
import random
import time

def greedy(path,cityMap):
    #print("\n\nStart of Greedy Algorithm")

    startTime = time.time()
    failToImprove = 0
    noPath = [0 for i in range(len(path))]
    tempPath = noPath.copy()
    

    #getRandomPath(tempPath)
    #shortestDistance = getPathDistance(tempPath,cityMap)
    #print("Random start, shortest distance:",shortestDistance)
    citiesToVisitStart = [i for i in range(len(path))]
    #print(f' cities to visit {citiesToVisitStart}')
    #for index in range(len(path)):
            #citiesToVisitStart[index] = index
    citiesToVisit = citiesToVisitStart.copy()
    startingCity = 0
    #print(f' temppath[0] {tempPath[0]}')
    citiesToVisit.remove(startingCity)
    #print(f' cities to visit {citiesToVisit}')


    print(f' temp path {tempPath}')
    #getGreedyPath(tempPath,citiesToVisit,cityMap)
    getGreedyMin(tempPath, citiesToVisit, cityMap, startingCity)
    print(f' temp path after getGreedyMin {tempPath}')

    tempDistance = getPathDistance(tempPath,cityMap)
    
    print("Distance:", tempDistance), 
    print(tempPath)
    
    shortestDistance = tempDistance
    path = tempPath.copy()
    tempDistance = 0
    limitOnTimesToFailToImprove = 1000

    while_counter = 0
    while(startingCity < len(path)):
        citiesToVisit = citiesToVisitStart.copy()
        #citiesToVisit = citiesToVisitStart
        print(f' while counter {while_counter}')
        tempPath = noPath.copy()
        #print("Cities to visit at start",citiesToVisit)

        tempPath[0] = startingCity
        citiesToVisit.remove(startingCity)
        
        startingCity = startingCity + 1
        
        print("Place to start:", tempPath[0])
        #print("Temp path",tempPath)
        #print("Cities to visit after picking random city",citiesToVisit)

        #getGreedyPath(tempPath,citiesToVisit,cityMap)
        getGreedyMin(tempPath,citiesToVisit, cityMap, startingCity)

        tempDistance = getPathDistance(tempPath,cityMap)
        
        print("Distance:", tempDistance), 
        #print(tempPath)
    
        if(tempDistance < shortestDistance):
            path = tempPath.copy()
            shortestDistance = tempDistance
            print("Shortest distance:",shortestDistance)
        else:
            failToImprove = failToImprove + 1
            print("Failed to improve.")
    while_counter += 1
    print(f' while_counter after {while_counter}')
    stopTime = time.time()
    print("Greedy Path:", path)
    distance = getPathDistance(path,cityMap)
    print("Greedy Distance:", distance)
    print("Greedy Time:", (stopTime - startTime))

def pickRandomCity(citiesToVisit):
    nextCity = random.choice(citiesToVisit)
    citiesToVisit.remove(nextCity)
    return nextCity
#def getGreedyMin2(tempPath, citiesToVisit, cityMap):


def getGreedyMin(tempPath, citiesToVisit, cityMap, startingCity):
    minArray = np.argmin(cityMap, axis=1)
    print(f' minarray {minArray[startingCity]}')
    nextCityIndex = minArray[startingCity]
    print(f' line 94 cities to visit {citiesToVisit}')
    while (len(citiesToVisit) != 0):
        if nextCityIndex in citiesToVisit and (tempPath[startingCity + 1] is not None):
            citiesToVisit.remove(nextCityIndex)
            print("This city has not been visited")

            tempPath[startingCity + 1] = nextCityIndex
            print(f' line 99 cities to visit {citiesToVisit}')
            #startingCity +=1
            startingCity = nextCityIndex
        else:
            cityMap[startingCity, nextCityIndex] = 100000
            print(cityMap)
            print("This city has been visited")
            getGreedyMin(tempPath, citiesToVisit, cityMap, startingCity)



    """for index in range((len(tempPath) - 1)):
        print("Where I am:", tempPath[index])
        print("Cities To Visit:", citiesToVisit)
        print(cityMap)
        nearestNeighborMax = np.amax(cityMap)
        print(f' nearest neighbor max is {nearestNeighborMax}')
        nearestNeighborMin = np.amin(cityMap[index])
        nearestNeighbor = nearestNeighborMin
        print(f'citymap[index is {cityMap[index]}')
        for checkIndex in range(len(citiesToVisit)):
            if (np.where(cityMap[index] == nearestNeighborMin) not in citiesToVisit) :
                nextCity = np.where(cityMap[index] == nearestNeighborMin)
                print(f'nearest neighbor is {nearestNeighbor}')
                print(f' next city is {nextCity}')
                nextCityIndex = int(nextCity[0])
                cityMap[tempPath[index]][citiesToVisit[checkIndex]] = nearestNeighborMax
                nearestNeighborMin = np.amin(cityMap[index])
                print(cityMap)
                print(f' new nearest Neighbor {nearestNeighborMin}')
                print(f' nextCityIndex is {nextCityIndex}')
                citiesToVisit.remove(nextCityIndex) """

         #nearestNeighbor = np.amin(cityMap[tempPath[index]][citiesToVisit[checkIndex]])
            #print(cityMap[tempPath[index]][citiesToVisit[checkIndex]])
            #print(f'new nearest neighbor{nearestNeighbor}')
            #nextDistance = cityMap[tempPath[index]][citiesToVisit[checkIndex]]
            #print("Next Distance", nextDistance)
            #if (nearestNeighbor == nextDistance):
                #nearestNeighbor = nextDistance
                #nextCity = citiesToVisit[checkIndex]
                #print(f'nearestNeighbor {nearestNeighbor}')
                #print(f'nextcity is {nextCity}')
                #break
        # load the winner from those cities to Visit
        #tempPath[index + 1] = nextCity
        #print("Updated temp path:", tempPath)
        #print("We go to:", nextCity)
        #citiesToVisit.remove(nextCity)



def getGreedyPath(tempPath,citiesToVisit,cityMap):
    #print("Working Greedy Algorithm (Meat)")
    nearestNeighborMax = np.amax(cityMap)
    for index in range((len(tempPath)-1)):
        print("Where I am:", tempPath[index])
        print("Cities To Visit:", citiesToVisit)
        print(cityMap)
        nearestNeighbor = nearestNeighborMax
        print(f'nearest neighbor is {nearestNeighbor}')
        for checkIndex in range(len(citiesToVisit)):
            nextDistance = cityMap[tempPath[index]][citiesToVisit[checkIndex]]
            print("Next Distance", nextDistance)
            if(nextDistance <= nearestNeighbor):
                nearestNeighbor = nextDistance
                nextCity = citiesToVisit[checkIndex]
                print(f'nextcity is {nextCity}')
        #load the winner from those cities to Visit
        tempPath[index+1] = nextCity
        #print("Updated temp path:", tempPath)
        #print("We go to:", nextCity)
        citiesToVisit.remove(nextCity)
