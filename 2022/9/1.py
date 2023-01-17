import math

def main():
    moves = read()
    positions = set()
    headPos = [0,0]
    tailPos = [0,0]

    for move in moves:
        for i in range(move[1]):
            if move[0] == 'U':
                headPos = [headPos[0], headPos[1] - 1]
                if math.dist(headPos, tailPos) >= 2:
                    tailPos = [headPos[0], headPos[1] + 1]
            elif move[0] == 'D':
                headPos = [headPos[0], headPos[1] + 1]
                if math.dist(headPos, tailPos) >= 2:
                    tailPos = [headPos[0], headPos[1] - 1]
            elif move[0] == 'L':
                headPos = [headPos[0] - 1, headPos[1]]
                if math.dist(headPos, tailPos) >= 2:
                    tailPos = [headPos[0] + 1, headPos[1]]    
            elif move[0] == 'R':
                headPos = [headPos[0] + 1, headPos[1]]
                if math.dist(headPos, tailPos) >= 2:
                    tailPos = [headPos[0] - 1, headPos[1]]
            positions.add("{}, {}".format(tailPos[0], tailPos[1]))

    print(len(positions))

def read():
    input = open("input.txt", "r")
    return [[dir, int(steps)] for (dir, steps) in list(line.split(" ") for line in input.read().splitlines())]

if __name__ == "__main__":
    main()