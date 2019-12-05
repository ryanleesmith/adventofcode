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

def _get_params(num_params):
    global data, pointer
    modes = [int(val) for val in str(data[pointer]).rjust(num_params + 2, '0')]
    params = []
    for i in range(num_params - 1, -1, -1):
        pointer += 1
        params.append(PARAM[int(modes[i])](pointer))
    return params

def _write(val):
    global data, pointer
    data[data[pointer]] = val
    pointer += 1

def _add():
    params = _get_params(3)
    _write(params[0] + params[1])

def _multiply():
    params = _get_params(3)
    _write(params[0] * params[1])

def _input():
    _get_params(1)
    _write(int(input("Provide input: ")))

def _output():
    global pointer
    params = _get_params(1)
    print(params[0])
    pointer += 1

def _jump(jump):
    global pointer
    params = _get_params(2)
    pointer = params[1] if (params[0] != 0) == jump else pointer + 1

def _less_than():
    params = _get_params(3)
    _write(1 if params[0] < params[1] else 0)

def _equals():
    params = _get_params(3)
    _write(1 if params[0] == params[1] else 0)

def _exit():
    print("Exit")
    raise SystemExit

OPCODE = {
    1: _add,
    2: _multiply,
    3: _input,
    4: _output,
    5: (lambda: _jump(True)),
    6: (lambda: _jump(False)),
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