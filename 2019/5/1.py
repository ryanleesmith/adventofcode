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
            pointer += 1
        except KeyError:
            print("KeyError")
            break

def _add():
    global data, pointer
    inst = str(data[pointer]).rjust(5, '0')
    x = PARAM[int(inst[2])](pointer + 1)
    y = PARAM[int(inst[1])](pointer + 2)
    data[data[pointer + 3]] = x + y
    pointer += 3

def _multiply():
    global data, pointer
    inst = str(data[pointer]).rjust(5, '0')
    x = PARAM[int(inst[2])](pointer + 1)
    y = PARAM[int(inst[1])](pointer + 2)
    data[data[pointer + 3]] = x * y
    pointer += 3

def _input():
    global data, pointer
    pointer += 1
    data[data[pointer]] = int(input("Provide input: "))

def _output():
    global data, pointer
    pointer += 1
    print(data[data[pointer]])

def _exit():
    global data
    print("Exit")
    raise SystemExit

OPCODE = {
    1: _add,
    2: _multiply,
    3: _input,
    4: _output,
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