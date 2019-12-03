import re
from collections import Counter

wires = []

class Wire:
    def __init__(self, movements):
        self.plot = [("0:0", 1)]
        self.steps = [("0:0", 0)]
        self.movements = movements

    def move(self):
        x = 0
        y = 0
        steps = 0
        for movement in self.movements:
            if movement.dir == "U":
                for i in range(1, movement.steps + 1, 1):
                    y += 1
                    self.plot.append((str(x) + ":" + str(y), 1))
                    steps += 1
                    self.steps.append((str(x) + ":" + str(y), steps))
            elif movement.dir == "D":
                for i in range(1, movement.steps + 1, 1):
                    y -= 1
                    self.plot.append((str(x) + ":" + str(y), 1))
                    steps += 1
                    self.steps.append((str(x) + ":" + str(y), steps))
            elif movement.dir == "L":
                for i in range(1, movement.steps + 1, 1):
                    x -= 1
                    self.plot.append((str(x) + ":" + str(y), 1))
                    steps += 1
                    self.steps.append((str(x) + ":" + str(y), steps))
            elif movement.dir == "R":
                for i in range(1, movement.steps + 1, 1):
                    x += 1
                    self.plot.append((str(x) + ":" + str(y), 1))
                    steps += 1
                    self.steps.append((str(x) + ":" + str(y), steps))\

    def __str__(self):
        return "".join([str(movement) for movement in self.movements])

class Movement:
    def __init__(self, data):
        self.dir = data[0]
        self.steps = int(data[1])

    def __str__(self):
        return self.dir + ": " + self.steps + "\n"

def main():
    global wires
    read()
    plots = []
    for wire in wires:
        wire.move()
        plots.append(wire.plot)

    count = sum((Counter(x) for x in [dict(x) for x in plots]), Counter())
    intersections = [x for x in count if count[x] >= 2 and x != '0:0']
    steps = []
    for intersection in intersections:
        count = 0
        for wire in wires:
            currSteps = sum((Counter(x) for x in [dict(x) for x in [wire.steps]]), Counter())
            count += [currSteps[x] for x in currSteps if x == intersection][0]

        steps.append(count)

    print(min(steps))

def read():
    global wires
    input = open("input.txt", "r")
    for line in input.read().splitlines():
        movements = []
        for movement in [str(movement) for movement in line.split(",")]:
            tuples = re.findall("([A-Z])(\d+)", movement)
            movements.append([Movement(movement) for movement in tuples][0])
        wires.append(Wire(movements))

if __name__ == "__main__":
    main()