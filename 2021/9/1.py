def main():
    heightmap = read()
    risk = 0
    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            if isLowest(row, col, heightmap):
                risk = risk + heightmap[row][col] + 1
    print(risk)

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
