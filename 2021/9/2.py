def main():
    heightmap = read()
    basins = []
    nines = []
    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            if isLowest(row, col, heightmap):
                basins.append([col, row])
            if heightmap[row][col] == 9:
                nines.append([col, row])
    sizes = []
    for basin in basins:
        distances = []
        for nine in nines:
            distances.append(abs(nine[0] - basin[0]) + abs(nine[1] - basin[1]))
        distances.sort()
        if basin[0] <= 1 or basin[1] <= 1 or basin[0] == len(heightmap[0]) - 2 or basin[1] == len(heightmap) - 2:
            dist = sum(distances[0:len(distances) / 2])
        else:
            dist = sum(distances)
        sizes.append([dist, basin])
    sizes.sort()
    print(sizes)

def isLowest(row, col, heightmap):
    if row - 1 != -1 and heightmap[row - 1][col] <= heightmap[row][col]:
        return False
    if row + 1 != len(heightmap) and heightmap[row + 1][col] <= heightmap[row][col]:
        return False
    if col - 1 != -1 and heightmap[row][col - 1] <= heightmap[row][col]:
        return False
    if col + 1 != len(heightmap[row]) and heightmap[row][col + 1] <= heightmap[row][col]:
        return False
    return True

def read():
    input = open("input.txt", "r")
    return [[int(i) for i in list(line)] for line in input.read().splitlines()]

if __name__ == "__main__":
    main()
