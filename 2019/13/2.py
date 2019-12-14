from os import system
import time
import numpy as np
from colorama import Fore, Style

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

grid = {}
score = 0

TILE = {
    0: " ",
    1: Style.BRIGHT + Fore.BLACK + u"\u2588",
    2: u"\u2588",
    3: Fore.RED + u"\u25AC",
    4: Fore.CYAN + u"\u25CF"
}

COLOR = {
    0: Fore.BLACK,
    1: Fore.RED,
    2: Fore.YELLOW,
    3: Fore.BLUE,
    4: Fore.MAGENTA,
    5: Fore.GREEN
}

def display():
    global grid, score
    system('clear')
    print(Style.BRIGHT + 'Score: ' + str(score) + Style.RESET_ALL)
    row = 0
    for y in range(24):
        line = f""
        for x in range(44):
            if grid[x][y] == 2:
                line += Style.BRIGHT + COLOR[(y - 2) % 6]
            line += TILE[grid[x][y]]
        print(line + Style.RESET_ALL)
    time.sleep(.01)
        
def main():
    global program, grid, score

    program = Program(read().copy())
    program.data[0] = 2

    counter = 0
    running = True
    x = None
    y = None
    ball = ()
    paddle = ()
    while running:
        try:
            program.run()
        except InputWait as iw:
            display()
            program.write(iw.pos, np.sign(ball[0] - paddle[0]))
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
                if _out == 3:
                    paddle = (x,y)
                if _out == 4:
                    ball = (x,y)
                grid[x][y] = _out % 5
            counter += 1
        except Finished:
            running = False

    display()

def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read().split(",")]

if __name__ == "__main__":
    main()