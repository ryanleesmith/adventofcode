import copy

seats = []

def main():
    global seats
    input = open("input.txt", "r")
    rows = [row for row in input.read().splitlines()]
    seats = [list(column) for column in rows]

    unchanged = True
    while unchanged:
        newSeats = copy.deepcopy(seats)
        unchanged = False
        for y in range(len(seats)):
            for x in range(len(seats[y])):
                if seats[y][x] == ".":
                    continue
                else:
                    occupied = getOccupied(x, y)
                    if seats[y][x] == "L" and occupied == 0:
                        newSeats[y][x] = "#"
                        unchanged = True
                    if seats[y][x] == "#" and occupied >= 4:
                        newSeats[y][x] = "L"
                        unchanged = True
        seats = newSeats
    total = 0
    for i in range(len(seats)):
        total = total + seats[i].count("#")
    print(total)

def getOccupied(x, y):
    global seats
    minX = max(0, x - 1)
    maxX = min(len(seats[0]) - 1, x + 1)
    minY = max(0, y - 1)
    maxY = min(len(seats) - 1, y + 1)

    count = 0
    for adjX in range(minX, maxX + 1):
        for adjY in range(minY, maxY + 1):
            if str(x) + ":" + str(y) != str(adjX) + ":" + str(adjY):
                if seats[adjY][adjX] == "#":
                    count = count + 1
    return count


if __name__ == "__main__":
    main()
