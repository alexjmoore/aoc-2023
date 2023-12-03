import collections
import math

def checkForSymbolandCog(lines, x, y):
    rows, cols = range(len(lines)),range(len(lines[0]))
    offsets = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for dy,dx in offsets:
        ny, nx = y+dy, x+dx
        if ny in rows and nx in cols:
            print(f"x:{nx},y:{ny}")
            c = lines[ny][nx]
            if isSymbol(c): return (True, isCog(c), nx, ny)
    return (False, False, 0, 0)

def isSymbol(char):
    return not ((char.isdigit()) or (char == '.'))

def isCog(char):
    return char == '*'

total = 0
allCogs = collections.defaultdict(list)
with open('testinput.txt') as input:
    lines = input.read().splitlines() 
    for y in range(len(lines)):
        currNumber = ""
        isPart = False
        cogsFound = {}
        for x in range(len(lines[y])):
            if lines[y][x].isdigit():
                currNumber += lines[y][x]
                if not isPart:
                    (isPart, nearCog, cogx, cogy) = checkForSymbolandCog(lines, x, y)
                    if nearCog:
                        cogsFound[(cogx,cogy)] = True
            
            if (not lines[y][x].isdigit()) or (x == len(lines[y])-1):
                if currNumber:
                    if isPart:
                        total += int(currNumber)
                        for cogs in cogsFound:
                            allCogs[cogs].append(int(currNumber))

                    currNumber = ""
                    isPart = False
                    cogsFound = {}
print(f"total: {total}")

ratios = 0
for i in allCogs:
    if len(allCogs[i]) > 1:
        ratios += math.prod(allCogs[i])
print(f"ratios: {ratios}")