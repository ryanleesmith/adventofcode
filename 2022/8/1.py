def main():
    data = read()
    rows = [[] for _ in range(len(data))]
    cols = [[] for _ in range(len(data[0]))]
    for y, row in enumerate(data):
        for x, height in enumerate(row):
            cols[x].append(height)
            rows[y].append(height)
    visible = ((len(data) - 2) * 2) + ((len(data[0]) - 2) * 2) + 4
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            maxLeft = max(rows[y][0:x])
            maxRight = max(rows[y][len(rows[y]):x:-1])
            maxUp = max(cols[x][0:y])
            maxDown = max(cols[x][len(cols[x]):y:-1])
            if data[y][x] > maxLeft or data[y][x] > maxRight or data[y][x] > maxUp or data[y][x] > maxDown:
                visible = visible + 1
    print(visible)

def read():
    input = open("input.txt", "r")
    return [[int(i) for i in list(line)] for line in input.read().splitlines()]

if __name__ == "__main__":
    main()
