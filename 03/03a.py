
def checkForSymbol(lines, x, y):
    if x > 0: 
        if isSymbol(lines[y][x-1]): return True
    if y > 0: 
        if isSymbol(lines[y-1][x]): return True
    if x < len(lines[y]) - 1:
        if isSymbol(lines[y][x+1]): return True
    if y < len(lines) - 1: 
        if isSymbol(lines[y+1][x]): return True
    if y > 0 and x > 0: 
        if isSymbol(lines[y-1][x-1]): return True
    if y > 0 and x < len(lines[y]) - 1: 
        if isSymbol(lines[y-1][x+1]): return True
    if y < len(lines) - 1 and x > 0: 
        if isSymbol(lines[y+1][x-1]): return True
    if y < len(lines) - 1 and x < len(lines[y]) - 1:
        if isSymbol(lines[y+1][x+1]): return True 
    return False

def isSymbol(char):
    return not ((char.isdigit()) or (char == '.'))

total = 0
with open('input.txt') as input:
    lines = input.read().splitlines() 
    for y in range(len(lines)):
        currNumber = ""
        isPart = False
        for x in range(len(lines[y])):
            if lines[y][x].isdigit():
                currNumber += lines[y][x]
                if not isPart:
                    isPart = checkForSymbol(lines, x, y)
            
            if (not lines[y][x].isdigit()) or (x == len(lines[y])-1):
                if currNumber:
                    if isPart:
                        total += int(currNumber)
                    currNumber = ""
                    isPart = False
                    
print(f"total: {total}")