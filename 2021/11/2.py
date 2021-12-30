octopi = []
flashed = []

def main():
    global octopi, flashed
    octopi = read()
    for i in range(1, 1000):
        flashed = []
        octopi = [map(lambda octopus: octopus + 1, row) for row in octopi]
        [map(lambda (x, octopus): flash(octopus, x, y), enumerate(row)) for (y, row) in enumerate(octopi)]
        octopi = [map(lambda octopus: 0 if octopus > 9 else octopus, row) for row in octopi]
        if sum([len(filter(lambda octopus: octopus == 0, row)) for row in octopi]) == 100:
            print(i)
            break

def flash(octopus, octopusX, octopusY):
    global octopi, flashed
    if octopus > 9 and (octopusX, octopusY) not in flashed:
        flashed.append((octopusX, octopusY))
        for y in range(octopusY - 1, octopusY + 2):
            if y < 0 or y == len(octopi):
                continue
            for x in range(octopusX - 1, octopusX + 2):
                if x < 0 or x == len(octopi[y]) or (x == octopusX and y == octopusY):
                    continue
                octopi[y][x] = octopi[y][x] + 1
                flash(octopi[y][x], x, y)

def read():
    input = open("input.txt", "r")
    return [[int(i) for i in list(line)] for line in input.read().splitlines()]

if __name__ == "__main__":
    main()
