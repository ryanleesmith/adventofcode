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

grid = {}

routine = ["A","B","A","C","B","C","A","C","B","C"]
movements = [["L","8","R","6","4","L","6","4"], ["R","6","4","L","8","L","8","L","6","4"], ["L","4","L","6","L","8","L","8"]]

def main():
    global program, grid

    program = Program(read().copy())
    program.data[0] = 2

    _in = []
    for i in routine:
        _in.append(ord(i))
        _in.append(ord(","))
    _in[len(_in) - 1] = 10

    for movement in movements:
        counter = 0
        for i in movement:
            _in.append(ord(i))
            _in.append(ord(","))
            counter += 1
        _in[len(_in) - 1] = 10

    pos = (0, 0)
    _out = ""
    _single_out = ""
    counter = 0
    finished = False
    while not finished:
        try:
            program.run()
        except InputWait as iw:
            if counter < len(_in):
                #print("Write: " + str(_in[counter]))
                program.write(iw.pos, _in[counter])
            elif counter == len(_in):
                program.write(iw.pos, ord("n"))
            else:
                program.write(iw.pos, 10)
            counter += 1
        except OutputWait as ow:
            if ow.output == 10:
                pos = (0, pos[1] + 1)
            else:
                grid[pos] = chr(ow.output)
                pos = (pos[0] + 1, pos[1])
            _out += chr(ow.output)
            _single_out = ow.output
        except Finished:
            finished = True

    print(_out)
    print(_single_out)

def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read().split(",")]

if __name__ == "__main__":
    main()