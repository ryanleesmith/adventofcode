import math

def main():
    moves = read()
    positions = set()
    knotPos = [[0,0] for _ in range(10)]

    for move in moves:
        for _ in range(move[1]):
            if move[0] == 'U':
                knotPos[0] = [knotPos[0][0], knotPos[0][1] - 1]
            elif move[0] == 'D':
                knotPos[0] = [knotPos[0][0], knotPos[0][1] + 1]
            elif move[0] == 'L':
                knotPos[0] = [knotPos[0][0] - 1, knotPos[0][1]]
            elif move[0] == 'R':
                knotPos[0] = [knotPos[0][0] + 1, knotPos[0][1]]
            for i in range(1,10):
                if math.dist(knotPos[i-1], knotPos[i]) >= 2:
                    x = y = None
                    if knotPos[i-1][0] - knotPos[i][0] == 2:
                        x = knotPos[i-1][0] - 1
                    elif knotPos[i-1][0] - knotPos[i][0] == -2:
                        x = knotPos[i-1][0] + 1
                    if knotPos[i-1][1] - knotPos[i][1] == 2:
                        y = knotPos[i-1][1] - 1
                    elif knotPos[i-1][1] - knotPos[i][1] == -2:
                        y = knotPos[i-1][1] + 1
                    if x == None:
                        x = knotPos[i-1][0]
                    if y == None:
                        y = knotPos[i-1][1]
                    knotPos[i] = [x, y]
            positions.add("{}, {}".format(knotPos[9][0], knotPos[9][1]))
    print(len(positions))

def read():
    input = open("input.txt", "r")
    return [[dir, int(steps)] for (dir, steps) in list(line.split(" ") for line in input.read().splitlines())]

if __name__ == "__main__":
    main()