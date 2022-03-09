import random
from array import array
# from GuessAndCheck import guessAndCheck
from LoadMap import loadMap
import numpy as np
import time

cityCount = 6
print("Our city count is", cityCount)
path = [0 for i in range(cityCount)]

cityMap = loadMap(cityCount)
print(cityMap)
print("If I didn't print out a city matrix, run me again!")

startingCity = 0
def determinePath(cityCount, cityMap):
    # Initialize an empty path
    path = [0 for i in range(cityCount)]
    distance =0;
    # Choose starting city
    startingCity = random.randint(0, cityCount)
    print(str(startingCity) + " is our starting city")
    # Add starting city to path
    path.clear()


    path.append(startingCity)

    print('Path: ' + str(path))
    for i in range(cityCount):
        print(path)
        # Find smallest distance to next city
        print('Find next smallest value')
        nextSmallestValue = np.min(cityMap[startingCity])
        print('The next closest distance is: ' + str(nextSmallestValue))
        distance += nextSmallestValue
        print(f'Total distance is {distance}')

        # Find the index
        print('Find the index of the next closest distance')
        nextCity = np.where(cityMap[startingCity] == nextSmallestValue)
        print('The Index of the next closest city is: ' + str(nextCity[0]))

        #Is the index in path?
        print('Index in path already? ' + str(nextCity in path))
        if (nextCity in path == True):
            print('Already in path, choose a different city')

            #nextCity = 10000
            #return path
        else:
            path.append(int(nextCity[0]))
            print(int(nextCity[0]))
            startingCity = int(nextCity[0])
            #return path
startTime = time.time()
determinePath(6, cityMap)
endTime = time.time()
elapsedTime = endTime - startTime
print(f'Total time was {elapsedTime}')
