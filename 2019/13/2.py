from os import system
import time
import numpy as np

program = []

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

def main():
    global program

    _labels = ["x", "y", "Tile"]
    _tiles = [" ", "|", u"\u2588", "_", "*"]

    program = Program(read().copy())
    program.data[0] = 2

    counter = 0
    running = True
    blocks = 0
    x = None
    y = None
    grid = {}
    ball = ()
    paddle = ()
    built = False
    score = 0
    while running or blocks > 0:
        #print("Blocks: " + str(blocks))
        try:
            program.run()
        except InputWait as iw:
            built = True
            system('clear')
            print(iw.pos)
            print("Score: " + str(score))
            for y in range(24):
                line = ""
                for x in range(44):
                    line += grid[x][y]
                print(line)

            #grid[ball[0]][ball[1]] = " "
            #ball = (ball[0] - 1, ball[1] - 1)
            #grid[ball[0]][ball[1]] = "*"

            print(np.sign(paddle[0] - ball[1]))
            program.write(iw.pos, np.sign(paddle[0] - ball[1]))

            #grid[paddle[0]][paddle[1]] = " "
            #paddle = (paddle[0] + move, paddle[1])
            #grid[paddle[0]][paddle[1]] = "_"

            #time.sleep(1)
        except OutputWait as ow:
            _out = ow.output
            if counter % 3 == 0:
                x = _out
            elif counter % 3 == 1:
                y = _out
            elif counter % 3 == 2 and x == -1 and y == 0:
                score = _out
            elif counter % 3 == 2:
                if not x in grid:
                    grid[x] = {}
                if not y in grid[x]:
                    grid[x][y] = {}
                if not built or _out == 3 or _out == 4:
                    grid[x][y] = _tiles[_out % 5]
                if _out == 3:
                    paddle = (x,y)
                if _out == 4:
                    ball = (x,y)
            if counter % 3 == 2 and _out == 2:
                blocks += 1
        except Finished:
            running = False
        counter += 1

def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read().split(",")]

if __name__ == "__main__":
    main()