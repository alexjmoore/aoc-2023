import re

conversion = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

PATTERN = r'^one|two|three|four|five|six|seven|eight|nine'

def checkpos(string, currnumber):
    if string[0].isdigit(): return int(string[0])
    if m := re.match(PATTERN, string): return(conversion[m.group(0)])
    return currnumber

total = 0
with open('input.txt') as input:
    while line := input.readline().strip():
        first = last = None
        while len(line) > 0:
            if not first: first = checkpos(line, first)
            last = checkpos(line, last)
            line = line[1:]        
        total += int(f"{first}{last}")
print(f"total: {total}")