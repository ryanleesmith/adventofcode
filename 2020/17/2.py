import copy

cubes = []
new_cubes = []

def main():
    global cubes
    input = open("input.txt", "r")
    for y, line in enumerate(input.read().splitlines()):
        for x, cube in enumerate(list(line)):
            if cube == "#":
                cubes.append((x, y, 0, 0))

    for _ in range(6):
        cycle()

    print(len(cubes))

def cycle():
    global cubes
    new_cubes = []
    for pos in cubes:
        active = getNeighbors(pos)
        if 2 <= active <= 3:
            new_cubes.append(pos)

    x_min = min(cubes, key=lambda cube: cube[0])[0] - 1
    x_max = max(cubes, key=lambda cube: cube[0])[0] + 2
    y_min = min(cubes, key=lambda cube: cube[1])[1] - 1
    y_max = max(cubes, key=lambda cube: cube[1])[1] + 2
    z_min = min(cubes, key=lambda cube: cube[2])[2] - 1
    z_max = max(cubes, key=lambda cube: cube[2])[2] + 2
    w_min = min(cubes, key=lambda cube: cube[3])[3] - 1
    w_max = max(cubes, key=lambda cube: cube[3])[3] + 2
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            for z in range(z_min, z_max):
                for w in range(w_min, w_max):
                    pos = (x, y, z, w)
                    if pos in cubes:
                        continue
                    active = getNeighbors(pos)
                    if active == 3:
                        new_cubes.append(pos)
    cubes = copy.deepcopy(new_cubes)

def getNeighbors(pos):
    global cubes
    active = 0
    for x in range(pos[0] - 1, pos[0] + 2):
        for y in range(pos[1] - 1, pos[1] + 2):
            for z in range(pos[2] - 1, pos[2] + 2):
                for w in range(pos[3] - 1, pos[3] + 2):
                    if (x, y, z, w) == pos:
                        continue
                    if (x, y, z, w) in cubes:
                        active = active + 1
    return active

if __name__ == "__main__":
    main()
