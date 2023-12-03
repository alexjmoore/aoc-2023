import collections
import math

def checkForSymbolandCog(lines, x, y):
    if x > 0: 
        c = lines[y][x-1]
        if isSymbol(c): return (True, isCog(c), x-1, y)
    if y > 0:
        c = lines[y-1][x]
        if isSymbol(c): return (True, isCog(c), x, y-1)
    if x < len(lines[y]) - 1:
        c = lines[y][x+1]
        if isSymbol(c): return (True, isCog(c), x+1, y)
    if y < len(lines) - 1: 
        c = lines[y+1][x]
        if isSymbol(c): return (True, isCog(c), x, y+1)
    if y > 0 and x > 0: 
        c = lines[y-1][x-1]
        if isSymbol(c): return (True, isCog(c), x-1, y-1)
    if y > 0 and x < len(lines[y]) - 1: 
        c = lines[y-1][x+1]
        if isSymbol(c): return (True, isCog(c), x+1, y-1)
    if y < len(lines) - 1 and x > 0: 
        c = lines[y+1][x-1]
        if isSymbol(c): return (True, isCog(c), x-1, y+1)
    if y < len(lines) - 1 and x < len(lines[y]) - 1:
        c = lines[y+1][x+1]
        if isSymbol(c): return (True, isCog(c), x+1, y+1)
    return (False, False, 0, 0)

def isSymbol(char):
    return not ((char.isdigit()) or (char == '.'))

def isCog(char):
    return char == '*'

total = 0
allCogs = collections.defaultdict(list)
with open('input.txt') as input:
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