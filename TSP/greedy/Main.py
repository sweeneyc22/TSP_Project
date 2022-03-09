from array import array
# from BruteForce import bruteForce
from GetPath import getRandomPath
from GetPathDistance import getPathDistance
from Greedy import greedy
# from GuessAndCheck import guessAndCheck
from LoadMap import loadMap

# from NoNoseAnt import noNoseAnt
# from Plan import displayPlan
# https://www.obeythetestinggoat.com/

cityCount = 6
rows, cols = (cityCount, cityCount)
cityMap = [[0 for i in range(cols)] for j in range(rows)]
path = [0 for i in range(cols)]

# displayPlan()
cityMap = loadMap(cityCount, cityMap)

# guessAndCheck(path,cityMap)
greedy(path, cityMap)
# bruteForce(path,cityMap)
# noNoseAnt(path,cityMap)
