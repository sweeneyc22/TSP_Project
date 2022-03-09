import random
from array import array
#from GuessAndCheck import guessAndCheck
from LoadMap import loadMap
import numpy as np
import bisect

print("Welcome to the Shortest Path program.")

cityCount = 6
print("Our city count is", cityCount)
path = [0 for i in range(cityCount)]

cityMap = loadMap(cityCount)
print(cityMap)
print("If I didn't print out a city matrix, run me again!")

startingCity = 0
#startingCity = random.randint(0, cityCount)
print(str(startingCity) + " is our starting city")

#search array pass in startingCity
#find min value based on row
#find location of that min
# add location to path
# find next lowest value
# check if lowest value location is not already in the path


def minRow(cityMap, cityCount):
    min = cityMap[0][0]
    minimum_Data = [0, 0, min]
    for i in range(cityCount):
        print(f' i is {i}.')

        print(f', i is {i}, current min is {min}.')

        for j in range(0,cityCount,1):
            print(f'i is {i}, j is {j}, city map is {cityMap[i][j]}.')
            if (cityMap[i][j] < min):
                min = cityMap[i][j]
                minimum_Data = [i, j, min]
                print(f'new minimum is {min}.')
        print(f'i is {i}, j is {j}, current min is {min}.')
    print(f'\n\n\n global min at {minimum_Data[0]},  {minimum_Data[1]}, is {minimum_Data[2]}.')
    return minimum_Data
minimum_Data = minRow(cityMap, cityCount)
print(f'the closest city to {minimum_Data[0]} is \
{minimum_Data[1]} with a distance of {cityMap[minimum_Data[0]][minimum_Data[1]]}.')

startingCity = minimum_Data[0]
nextCity = minimum_Data[1]


print("new")
#startingCity = cityMap[0]
print('Starting city: ' + str(startingCity))

#Begin at the first city
#nextCity = startingCity

#Find the min val of cityMap[0]
print(str(cityMap[0].min()))

#set the next city with smallest dist
min = np.min(cityMap[0])

print(str(min))

#Find the index of the min val
closestCity = np.where(cityMap[0] == min)
print('first closest city' + str(closestCity))

path = int(closestCity[0])
print (path)


nextCity = closestCity
print(str(cityMap[nextCity].min()))
min = np.min(cityMap[nextCity])
closestCity = np.where(cityMap[nextCity] == min)
print('next closest city'+ str(closestCity))


print('test case')
startingCity = 0
print('City: ' + str(cityMap[0]))



for j in range(0, len(cityMap[startingCity])):

       # print('City: ' + str(j))
        print('j: ' + str(j))
        print('nextCityDistance: ' + str(cityMap[1][j]))
        if int(cityMap[1][j]) < int(cityMap[1][j+1]):
            print('Index at City[ ' + str(j) + '] is smaller')
            temp = cityMap[1][j]
            print(temp)













