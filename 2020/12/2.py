import re
import math
import numpy as np

pos = (0, 0)
waypoint = (10, -1)

def main():
    global pos, waypoint

    input = open("input.txt", "r")
    instructions = [[x for x in re.findall("([A-Z])(\d+)", line)][0] for line in input.read().splitlines()]

    for instruction in instructions:
        if instruction[0] == "L":
            waypoint = rotate(waypoint, math.radians(int(instruction[1])))
        elif instruction[0] == "R":
            waypoint = rotate(waypoint, math.radians(int(instruction[1]) * -1))
        elif instruction[0] == "F":
            moveShip(int(instruction[1]))
        else:
            moveWaypoint(instruction[0], int(instruction[1]))
    
    print(abs(pos[0]) + abs(pos[1]))

def moveShip(multiple):
    global pos, waypoint
    pos = (pos[0] + (waypoint[0] * multiple), pos[1] + (waypoint[1] * multiple))

def moveWaypoint(direction, distance):
    global waypoint
    if direction == "N":
        waypoint = (waypoint[0], waypoint[1] - distance)
    elif direction == "E":
        waypoint = (waypoint[0] + distance, waypoint[1])
    elif direction == "S":
        waypoint = (waypoint[0], waypoint[1] + distance)
    elif direction == "W":
        waypoint = (waypoint[0] - distance, waypoint[1])

def rotate(xy, radians):
    x, y = xy
    c, s = np.cos(radians), np.sin(radians)
    j = np.matrix([[c, s], [-s, c]])
    m = np.dot(j, [x, y])

    return (int(round(float(m.T[0]), 0)), int(round(float(m.T[1]), 0)))

if __name__ == "__main__":
    main()
