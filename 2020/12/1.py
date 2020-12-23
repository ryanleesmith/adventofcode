import re

DIRECTIONS = ["N", "E", "S", "W"]
pos = (0, 0)

def main():
    global pos, DIRECTIONS
    input = open("input.txt", "r")
    instructions = [[x for x in re.findall("([A-Z])(\d+)", line)][0] for line in input.read().splitlines()]

    facing = 1
    for instruction in instructions:
        if instruction[0] == "L":
            facing = facing - (int(instruction[1]) / 90)
        elif instruction[0] == "R":
            facing = facing + (int(instruction[1]) / 90)
        elif instruction[0] == "F":
            move(DIRECTIONS[facing % 4], int(instruction[1]))
        else:
            move(instruction[0], int(instruction[1]))
    
    print(abs(pos[0]) + abs(pos[1]))

def move(direction, distance):
    global pos
    if direction == "N":
        pos = (pos[0], pos[1] - distance)
    elif direction == "E":
        pos = (pos[0] + distance, pos[1])
    elif direction == "S":
        pos = (pos[0], pos[1] + distance)
    elif direction == "W":
        pos = (pos[0] - distance, pos[1])

if __name__ == "__main__":
    main()
