def main():
    data = read()
    rows = [[] for _ in range(len(data))]
    cols = [[] for _ in range(len(data[0]))]
    for y, row in enumerate(data):
        for x, height in enumerate(row):
            cols[x].append(height)
            rows[y].append(height)
    best = 0
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            leftIdx = next((idx + 1 for idx, val in enumerate(rows[y][x-1::-1]) if val >= data[y][x]), x)
            rightIdx = next((idx + 1 for idx, val in enumerate(rows[y][x+1:len(rows[y])]) if val >= data[y][x]), len(rows[y]) - 1 - x)
            upIdx = next((idx + 1 for idx, val in enumerate(cols[x][y-1::-1]) if val >= data[y][x]), y)
            downIdx = next((idx + 1 for idx, val in enumerate(cols[x][y+1:len(cols[x])]) if val >= data[y][x]), len(cols[x]) - 1 - y)
            score = leftIdx * rightIdx  * upIdx * downIdx
            best = max(score, best)
    print(best)

def read():
    input = open("input.txt", "r")
    return [[int(i) for i in list(line)] for line in input.read().splitlines()]

if __name__ == "__main__":
    main()
