data = []
pointer = 0

def main():
    global data, pointer

    data = read()
    while pointer < len(data):
        try:
            inst = str(data[pointer]).rjust(2, '0')
            opcode = int(inst[len(inst) - 2] + inst[len(inst) - 1])
            OPCODE[opcode]()
        except KeyError:
            print("KeyError")
            break

def _inc_pointer():
    global pointer
    pointer += 1

def _add():
    global data, pointer
    inst = str(data[pointer]).rjust(5, '0')
    _inc_pointer()
    x = PARAM[int(inst[2])](pointer)
    _inc_pointer()
    y = PARAM[int(inst[1])](pointer)
    _inc_pointer()
    data[data[pointer]] = x + y
    _inc_pointer()

def _multiply():
    global data, pointer
    inst = str(data[pointer]).rjust(5, '0')
    _inc_pointer()
    x = PARAM[int(inst[2])](pointer)
    _inc_pointer()
    y = PARAM[int(inst[1])](pointer)
    _inc_pointer()
    data[data[pointer]] = x * y
    _inc_pointer()

def _input():
    global data, pointer
    _inc_pointer()
    data[data[pointer]] = int(input("Provide input: "))
    _inc_pointer()

def _output():
    global data, pointer
    inst = str(data[pointer]).rjust(3, '0')
    _inc_pointer()
    x = PARAM[int(inst[0])](pointer)
    _inc_pointer()
    print(x)

def _jump_true():
    global data, pointer
    inst = str(data[pointer]).rjust(4, '0')
    _inc_pointer()
    x = PARAM[int(inst[1])](pointer)
    _inc_pointer()
    y = PARAM[int(inst[0])](pointer)
    _inc_pointer()
    if x != 0:
        pointer = y

def _jump_false():
    global data, pointer
    inst = str(data[pointer]).rjust(4, '0')
    _inc_pointer()
    x = PARAM[int(inst[1])](pointer)
    _inc_pointer()
    y = PARAM[int(inst[0])](pointer)
    _inc_pointer()
    if x == 0:
        pointer = y

def _less_than():
    global data, pointer
    inst = str(data[pointer]).rjust(5, '0')
    _inc_pointer()
    x = PARAM[int(inst[2])](pointer)
    _inc_pointer()
    y = PARAM[int(inst[1])](pointer)
    _inc_pointer()
    if x < y:
        data[data[pointer]] = 1
    else:
        data[data[pointer]] = 0
    _inc_pointer()

def _equals():
    global data, pointer
    inst = str(data[pointer]).rjust(5, '0')
    _inc_pointer()
    x = PARAM[int(inst[2])](pointer)
    _inc_pointer()
    y = PARAM[int(inst[1])](pointer)
    _inc_pointer()
    if x == y:
        data[data[pointer]] = 1
    else:
        data[data[pointer]] = 0
    _inc_pointer()

def _exit(*argv):
    global data
    print("Exit")
    raise SystemExit

OPCODE = {
    1: _add,
    2: _multiply,
    3: _input,
    4: _output,
    5: _jump_true,
    6: _jump_false,
    7: _less_than,
    8: _equals,
    99: _exit
}

PARAM = {
    0: (lambda pos: data[data[pos]]),
    1: (lambda pos: data[pos])
}

def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read().split(",")]

if __name__ == "__main__":
    main()