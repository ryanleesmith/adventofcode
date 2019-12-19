from os import system
import time
import numpy as np

class InputWait(Exception):
    def __init__(self, pos):
        self.pos = pos

class OutputWait(Exception):
    def __init__(self, output):
        self.output = output

class Finished(Exception):
    pass

class Program:
    PARAM = {
        0: (lambda data, pos, base: data[pos]),
        1: (lambda data, pos, base: pos),
        2: (lambda data, pos, base: data[pos] + base),
    }

    def __init__(self, data):
        self.data = data
        self.data.extend(0 for _ in range(10000))
        self.pointer = 0
        self.base = 0
        self.running = False

    def run(self):
        self.running = True

        while self.running:
            while self.pointer < len(self.data):
                try:
                    inst = str(self.data[self.pointer]).rjust(2, '0')
                    opcode = int(inst[len(inst) - 2] + inst[len(inst) - 1])
                    if opcode == 1:
                        self.add()
                    if opcode == 2:
                        self.multiply()
                    if opcode == 3:
                        self.input()
                    if opcode == 4:
                        self.output()
                    if opcode == 5:
                        self.jump(True)
                    if opcode == 6:
                        self.jump(False)
                    if opcode == 7:
                        self.less_than()
                    if opcode == 8:
                        self.equals()
                    if opcode == 9:
                        self.adjust()
                    if opcode == 99:
                        self.exit()
                except KeyError:
                    print("KeyError")
                    break

    def get_params(self, num_params):
        modes = [int(val) for val in str(self.data[self.pointer]).rjust(num_params + 2, '0')]
        params = []
        for i in range(num_params - 1, -1, -1):
            self.pointer += 1
            param = None
            try:
                param = Program.PARAM[int(modes[i])](self.data, self.pointer, self.base)
            except IndexError as ie:
                pass
            params.append(param)
        return params

    def write(self, pos, val):
        self.data[pos] = val
        self.pointer += 1

    def add(self):
        params = self.get_params(3)
        self.write(params[2], self.data[params[0]] + self.data[params[1]])

    def multiply(self):
        params = self.get_params(3)
        self.write(params[2], self.data[params[0]] * self.data[params[1]])

    def input(self):
        params = self.get_params(1)
        self.running = False
        raise InputWait(params[0])

    def send(self, _input):
        self.write(_input)

    def output(self):
        params = self.get_params(1)
        self.pointer += 1
        self.running = False
        raise OutputWait(self.data[params[0]])

    def jump(self, do_jump):
        params = self.get_params(2)
        self.pointer = self.data[params[1]] if (self.data[params[0]] != 0) == do_jump else self.pointer + 1

    def less_than(self):
        params = self.get_params(3)
        self.write(params[2], 1 if self.data[params[0]] < self.data[params[1]] else 0)

    def equals(self):
        params = self.get_params(3)
        self.write(params[2], 1 if self.data[params[0]] == self.data[params[1]] else 0)

    def adjust(self):
        params = self.get_params(1)
        self.base += self.data[params[0]]
        self.pointer += 1

    def exit(self):
        self.running = False
        raise Finished

def display():
    global grid, blocked, moves
    system('clear')
    for y in range(-21, 20):
        line = ""
        for x in range(-21, 20):
            if (x, y) in grid:
                line += grid[(x, y)]
            else:
                line += " "
        print(line)

def move(response):
    global grid, direction, adjustment, pos, blocked, moves, oxygen
    if response == 0:
        x = pos[0] + adjustment[direction % 4][0]
        y = pos[1] + adjustment[direction % 4][1]
        grid[(x, y)] = "#"

        new = False
        counter = 0
        while not new:
            direction += 1
            x = pos[0] + adjustment[direction % 4][0]
            y = pos[1] + adjustment[direction % 4][1]
            if not (x, y) in grid:
                new = True
            if (counter > 4 and grid[x, y] == "."):
                new = True
                blocked = True
                if grid[pos] != "O":
                    grid[pos] = "_"
            if counter > 8:
                return False
            counter += 1
    elif response == 1 or response == 2:
        explored = False
        if not blocked and pos in grid and grid[pos] != "_" and grid[pos] != "O":
            grid[pos] = "."
        x = pos[0] + adjustment[direction % 4][0]
        y = pos[1] + adjustment[direction % 4][1]
        pos = (x, y)
        if response == 2:
            oxygen = pos
        if not pos in grid:
            moves += 1
        else:
            moves -= 1
        grid[pos] = "x"
        if not blocked:
            op = adjustment[(direction + 2) % 4]
            test = (pos[0] + (op[0] * 2), pos[1] + (op[1] * 2))
            if test in grid and (grid[test] == "_" or grid[test] == "/"):
                path = 0
                for i in adjustment:
                    check = (pos[0] + op[0] + i[0], pos[1] + op[1] + i[1])
                    if not check in grid or grid[check] == "." or grid[check] == "x":
                        path += 1
                if path < 2:
                    grid[(pos[0] + op[0], pos[1] + op[1])] = "/"
                    blocked = True
        if blocked:
            blocked = False
            open = None
            counter = 0
            for i in adjustment:
                test = (pos[0] + i[0], pos[1] + i[1])
                if not test in grid:
                    open = None
                    break
                elif grid[test] == ".":
                    open = direction
                    op = adjustment[open % 4]
                    test = (pos[0] + op[0], pos[1] + op[1])
                    if test in grid and grid[test] == "_":
                        open = counter
                        grid[pos] = "_"
                        blocked = True
                counter += 1
            if open != None:
                direction = open
            else:
                direction = counter
        elif explored:
            open = None
            counter = 0
            for i in adjustment:
                test = (pos[0] + i[0], pos[1] + i[1])
                if not test in grid:
                    open = None
                    break
                elif grid[test] == ".":
                    open = counter
                counter += 1
            if open != None:
                direction = open
            else:
                direction = counter
    return True

def spread():
    global grid, adjustment, minutes

    minutes += 1

    oxygens = []
    for y in range(-21, 20):
        for x in range(-21, 20):
            pos = (x, y)
            if grid[pos] == "O":
                for i in adjustment:
                    new = (pos[0] + i[0], pos[1] + i[1])
                    if grid[new] == " ":
                        oxygens.append(new)
    for oxygen in oxygens:
        grid[oxygen] = "O"

def full():
    global grid

    for y in range(-21, 20):
        for x in range(-21, 20):
            pos = (x, y)
            if grid[pos] == " ":
                return False
    return True

program = []
grid = {(0, 0): "x"}
direction = 0
directions = [1, 4, 2, 3]
adjustment = [(0, -1), (1, 0), (0, 1), (-1, 0)]
pos = (0,0)
blocked = False
moves = 0
oxygen = None
minutes = 0
        
def main():
    global program, grid, direction, directions, pos

    program = Program(read().copy())

    found = False
    while not found:
        try:
            program.run()
        except InputWait as iw:
            program.write(iw.pos, directions[direction % 4])
        except OutputWait as ow:
            _out = ow.output
            if not move(_out):
                found = True
            display()
        except Finished:
            found = True
    for y in range(-21, 20):
        for x in range(-21, 20):
            if (x, y) in grid:
                if grid[(x, y)] == "_" or grid[(x, y)] == "/":
                    grid[(x, y)] = " "
            else:
                grid[(x, y)] = "#"

    grid[oxygen] = "O"
    grid[pos] = " "
    display()

    while not full():
        spread()
        display()

def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read().split(",")]

if __name__ == "__main__":
    main()