MAX_COLOUR_COUNT = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

total = 0
with open('input.txt') as input:
    while line := input.readline().strip():
        (game, results) = line.split(':')
        game = int(game.split(' ')[1].strip())
        cubesets = results.split(';')
        invalidGame = False
        for cubes in cubesets:
            for cube in cubes.split(','):
                (count, colour) = cube.strip().split(' ')
                if int(count.strip()) > MAX_COLOUR_COUNT[colour]:
                    invalidGame = True
                    break
        if not invalidGame: total += game
print(f"total: {total}")