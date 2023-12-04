import collections
cardCounts = collections.defaultdict(lambda: 1)
with open('input.txt') as input:
    for line in (lines := input.read().splitlines()):
        (game, card) = line.split(':')
        game = int(game.split()[1])
        (winners, numbers) = card.split('|')
        winners = winners.split()
        numbers = numbers.split()
        matchedNumbersCount = len(set(winners).intersection(numbers))
        for i in range(cardCounts[game]):
            for x in (range(matchedNumbersCount)):
                cardCounts[game+x+1] += 1
print(f"total: {sum(cardCounts.values())}")