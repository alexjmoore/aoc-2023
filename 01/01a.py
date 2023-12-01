import re
total = 0
with open('input.txt') as input:
    while line := input.readline().strip():
        numbers = re.findall(r'(\d)', line)
        total += int(f"{numbers[0]}{numbers[-1]}")
print(f"total: {total}")