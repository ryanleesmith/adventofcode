import copy

seats = []
maxX = 0
maxY = 0

def main():
    global seats, maxX, maxY
    input = open("input.txt", "r")
    rows = [row for row in input.read().splitlines()]
    seats = [list(column) for column in rows]

    maxX = len(seats[0]) - 1
    maxY = len(seats) - 1

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
                    if seats[y][x] == "#" and occupied >= 5:
                        newSeats[y][x] = "L"
                        unchanged = True
        seats = newSeats
    total = 0
    for i in range(len(seats)):
        total = total + seats[i].count("#")
    print(total)

def getOccupied(x, y):
    global seats, maxX, maxY

    count = 0
    for adjX in range(x - 1, -1, -1):
        if seats[y][adjX] == "#":
            count = count + 1
            break
        elif seats[y][adjX] == "L":
            break
    for adjX in range(x + 1, maxX + 1):
        if seats[y][adjX] == "#":
            count = count + 1
            break
        elif seats[y][adjX] == "L":
            break
    for adjY in range(y - 1, -1, -1):
        if seats[adjY][x] == "#":
            count = count + 1
            break
        elif seats[adjY][x] == "L":
            break
    for adjY in range(y + 1, maxY + 1):
        if seats[adjY][x] == "#":
            count = count + 1
            break
        elif seats[adjY][x] == "L":
            break
    offset = 1
    for adjX in range(x - 1, -1, -1):
        adjY = y - offset
        if adjY < 0:
            break
        offset = offset + 1
        if seats[adjY][adjX] == "#":
            count = count + 1
            break
        elif seats[adjY][adjX] == "L":
            break
    offset = 1
    for adjX in range(x + 1, maxX + 1):
        adjY = y + offset
        if adjY > maxY:
            break
        offset = offset + 1
        if seats[adjY][adjX] == "#":
            count = count + 1
            break
        elif seats[adjY][adjX] == "L":
            break
    offset = 1
    for adjY in range(y - 1, -1, -1):
        adjX = x + offset
        if adjX > maxX:
            break
        offset = offset + 1
        if seats[adjY][adjX] == "#":
            count = count + 1
            break
        elif seats[adjY][adjX] == "L":
            break
    offset = 1
    for adjY in range(y + 1, maxY + 1):
        adjX = x - offset
        if adjX < 0:
            break
        offset = offset + 1
        if seats[adjY][adjX] == "#":
            count = count + 1
            break
        elif seats[adjY][adjX] == "L":
            break
    return count

if __name__ == "__main__":
    main()
