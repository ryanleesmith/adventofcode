from itertools import permutations

phase_sets = list(permutations([5, 6, 7, 8, 9]))

amps = []

program = []
programs = []
pointer = 0

_in = 0
_out = 0

num_outputs = 0
phase = 0

_max = 0
_max_phases = None

class InputWait(Exception):
    pass

class OutputWait(Exception):
    def __init__(self, output):
        self.output = output

class Finished(Exception):
    pass

class Amp:
    def __init__(self, phase, program):
        self.phase = phase
        self.program = Program(program)
        self.finished = False

    def start(self):
        try:
            self.program.run()
        except InputWait:
            self.send(self.phase)
            self.program.run()

    def send(self, _input):
        self.program.send(_input)

    def run(self):
        try:
            self.program.run()
        except Finished:
            self.finished = True

class Program:
    PARAM = {
        0: (lambda data, pos: data[data[pos]]),
        1: (lambda data, pos: data[pos])
    }

    def __init__(self, data):
        self.data = data
        self.pointer = 0
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
            params.append(Program.PARAM[int(modes[i])](self.data, self.pointer))
        return params

    def write(self, val):
        self.data[self.data[self.pointer]] = val
        self.pointer += 1

    def add(self):
        params = self.get_params(3)
        self.write(params[0] + params[1])

    def multiply(self):
        params = self.get_params(3)
        self.write(params[0] * params[1])

    def input(self):
        #print("Needs Input")
        self.get_params(1)
        self.running = False
        raise InputWait

    def send(self, _input):
        #print("Sent " + str(_input))
        self.write(_input)

    def output(self):
        params = self.get_params(1)
        self.pointer += 1
        self.running = False
        raise OutputWait(params[0])

    def jump(self, do_jump):
        params = self.get_params(2)
        self.pointer = params[1] if (params[0] != 0) == do_jump else self.pointer + 1

    def less_than(self):
        params = self.get_params(3)
        self.write(1 if params[0] < params[1] else 0)

    def equals(self):
        params = self.get_params(3)
        self.write(1 if params[0] == params[1] else 0)

    def exit(self):
        #print("Exit")
        self.running = False
        raise Finished

def main():
    global programs, program, pointer, _in, _out, _max, _max_phases, num_outputs, amps, phase_sets

    program = read()

    for phase_set in phase_sets:
        amps = []
        for phase in phase_set:
            try:
                amp = Amp(phase, program.copy())
                amp.start()
            except InputWait:
                pass
            amps.append(amp)

        running = True
        amp = 0
        out = 0
        send_start = True

        while running:
            try:
                if send_start:
                    amps[amp].send(out)
                    send_start = False
                amps[amp].run()
            except InputWait:
                continue
            except OutputWait as ow:
                try:
                    amps[amp].run()
                except InputWait:
                    pass
                out = ow.output
                amp += 1
                if amp >= len(amps):
                    amp = 0
                if not amps[amp].finished:
                    amps[amp].send(out)
                continue
            if amps[amp].finished:
                amp += 1
                if amp >= len(amps):
                    running = False

        if out > _max:
            _max = out

    print(_max)

def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read().split(",")]

if __name__ == "__main__":
    main()