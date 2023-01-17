minX = maxX = maxY = None
rocks = set()
sand = set()

def main():
    global minX, maxX, maxY, rocks, sand

    data = read()
    minX = maxX = maxY = None
    for group in data:
        startX = startY = None
        for coord in group:
            if startX != None:
                if coord[0] == startX:
                    dist = coord[1] - startY
                    if dist > 0:
                        for y in range(0, dist + 1):
                            maxY = max(startY + y, maxY) if maxY != None else startY + y
                            rocks.add("{},{}".format(startX, startY + y))
                    else:
                        for y in range(0, dist - 1, -1):
                            maxY = max(startY + y, maxY) if maxY != None else startY + y
                            rocks.add("{},{}".format(startX, startY + y))
                else:
                    dist = coord[0] - startX
                    if dist > 0:
                        for x in range(0, dist + 1):
                            minX = min(startX + x, minX) if minX != None else startX + x
                            maxX = max(startX + x, maxX) if maxX != None else startX + x
                            rocks.add("{},{}".format(startX + x, startY))
                    else:
                        for x in range(0, dist - 1, -1):
                            minX = min(startX + x, minX) if minX != None else startX + x
                            maxX = max(startX + x, maxX) if maxX != None else startX + x
                            rocks.add("{},{}".format(startX + x, startY))
            startX = coord[0]
            startY = coord[1]

    for _ in range(962):
        x = 500
        for y in range(maxY + 1):
            if "{},{}".format(x, y) in rocks or "{},{}".format(x, y) in sand:
                if "{},{}".format(x - 1, y) not in rocks and "{},{}".format(x - 1, y) not in sand:
                    x = x - 1
                    y = y + 1
                    continue
                elif "{},{}".format(x + 1, y) not in rocks and "{},{}".format(x + 1, y) not in sand:
                    x = x + 1
                    y = y + 1
                    continue
                break
        if (y - 1) == maxY:
            break
        sand.add("{},{}".format(x, y - 1))
    display()
    print(len(sand) - 1)

def display():
    global minX, maxX, maxY, rocks, sand
    output = ""
    for y in range(maxY + 1):
        for x in range(minX, maxX + 1):
            if "{},{}".format(x, y) in rocks:
                output = output + "#"
            elif "{},{}".format(x, y) in sand:
                output = output + "o"
            else:
                output = output + ("." if "{},{}".format(x, y) != "500,0" else "+")
        output = output + "\r\n"
    print(output)

def read():
    input = open("input.txt", "r")
    ret = [[i for i in line.split(" -> ")] for line in input.read().splitlines()]
    ret = [[i.split(",") for i in line] for line in ret]
    ret = [[[int(x), int(y)] for (x, y) in list(i)] for i in ret]
    return ret

if __name__ == "__main__":
    main()
