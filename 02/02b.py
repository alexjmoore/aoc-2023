total = 0
with open('input.txt') as input:
    while line := input.readline().strip():
        (game, results) = line.split(':')
        game = int(game.split(' ')[1].strip())
        cubesets = results.split(';')
        peakColours = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for cubes in cubesets:
            for cube in cubes.split(','):
                (count, colour) = cube.strip().split(' ')
                if int(count.strip()) > peakColours[colour]: peakColours[colour] = int(count.strip())
        total += (peakColours['red'] * peakColours['green'] * peakColours['blue'])
print(f"total: {total}")