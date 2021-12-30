def main():
    data = read()

def read():
    input = open("input.txt", "r")
    maxX = 0
    maxY = 0
    lines = []
    for line in input.read().splitlines():
        line = [[int(x), int(y)] for (x, y) in list(i.split(",") for i in line.split(" -> "))]
        lines.append(line)
        maxX = max(max(maxX, line[0][0]), line[1][0])
        maxY = max(max(maxY, line[0][1]), line[1][1])

    grid = [[0] * (maxX + 1) for i in range(maxY + 1)]
    for line in lines:
        if line[0][0] == line[1][0]:
            start = line[0][1]
            end = line[1][1] + 1 if line[0][1] < line[1][1] else line[1][1] - 1
            for i in range(start, end, 1 if line[0][1] < line[1][1] else -1):
                grid[i][line[0][0]] = grid[i][line[0][0]] + 1
        elif line[0][1] == line[1][1]:
            start = line[0][0]
            end = line[1][0] + 1 if line[0][0] < line[1][0] else line[1][0] - 1
            for i in range(start, end, 1 if line[0][0] < line[1][0] else -1):
                grid[line[0][1]][i] = grid[line[0][1]][i] + 1
        else:
            start = line[0][0]
            end = line[1][0] + 1 if line[0][0] < line[1][0] else line[1][0] - 1
            yStart = line[0][1]
            yStep = 1 if line[0][1] < line[1][1] else -1
            for i in range(start, end, 1 if line[0][0] < line[1][0] else -1):
                grid[yStart][i] = grid[yStart][i] + 1
                yStart = yStart + yStep

    count = 0
    for row in grid:
        for col in row:
            if col >= 2:
                count = count + 1
    print(count)
if __name__ == "__main__":
    main()
