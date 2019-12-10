program = []

_in = 0
_out = 0

class InputWait(Exception):
    pass

class OutputWait(Exception):
    def __init__(self, output):
        self.output = output

class Finished(Exception):
    pass

class Program:
    #PARAM = {
    #    0: (lambda data, pos, base: data[data[pos]]),
    #    1: (lambda data, pos, base: data[pos]),
    #    2: (lambda data, pos, base: data[data[pos] + base]),
    #}

    PARAM = {
        0: (lambda data, pos, base: data[pos]),
        1: (lambda data, pos, base: pos),
        2: (lambda data, pos, base: data[pos] + base),
    }

    def __init__(self, data):
        self.data = data
        self.data.extend(0 for _ in range(10000000))
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
                    #print("Running: " + str(opcode))
                    #print("Pointer at: " + str(self.pointer))
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
                #extend = None
                #if int(modes[i]) == 0:
                #    extend = self.data[self.pointer]
                #if int(modes[i]) == 1:
                #    extend = self.pointer
                #if int(modes[i]) == 2:
                #    extend = self.data[self.pointer + self.base]
                #self.data.extend(0 for _ in range(extend + 1))
                #print("Extending by: " + str(extend))
                #param = 0
            params.append(param)
        return params

    def write(self, pos, val):
        #print("Write: " + str(val) + " to " + str(self.data[self.pointer]))
        self.data[pos] = val
        self.pointer += 1

    def add(self):
        params = self.get_params(3)
        #print("Add: " + str(params[0]) + " " + str(params[1]))
        self.write(params[2], self.data[params[0]] + self.data[params[1]])

    def multiply(self):
        params = self.get_params(3)
        self.write(params[2], self.data[params[0]] * self.data[params[1]])

    def input(self):
        #print("Needs Input")
        params = self.get_params(1)
        self.write(params[0], 1)
        self.running = False
        raise InputWait

    def send(self, _input):
        #print("Sent " + str(_input))
        self.write(_input)

    def output(self):
        params = self.get_params(1)
        #print("Get output at: " + str(params[0]))
        #print(str(self.data[params[0]]))
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
        #print("Base: " + str(self.base))
        self.pointer += 1

    def exit(self):
        #print("Exit")
        self.running = False
        raise Finished

def main():
    global program, _in, _out

    program = Program(read().copy())

    running = True
    while running:
        try:
            program.run()
        except InputWait:
            #print("Input?")
            #print(program.pointer)
            #program.send(1)
            continue
        except OutputWait as ow:
            _out = ow.output
            print("Out: " + str(_out))
            #print("Pointer: " + str(program.pointer))
            #program.send(_out)
            continue
        except Finished:
            running = False

    #print(_out)

def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read().split(",")]

if __name__ == "__main__":
    main()