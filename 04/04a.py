total = 0
with open('input.txt') as input:
    for line in (lines := input.read().splitlines()):
        (winners, numbers) = line.split(':')[1].split('|')
        winners = winners.split()
        numbers = numbers.split()
        result = 0
        matchedNumbersCount = len(set(winners).intersection(numbers))
        if matchedNumbersCount > 0:
            result = 1 * (2**(matchedNumbersCount - 1))
        total += result
print(f"total: {total}")