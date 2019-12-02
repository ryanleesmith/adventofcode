data = []
noun = 0
verb = 0

def main():
    global data, noun, verb
    for noun, verb in pairs():
        data = read()
        data[1] = noun
        data[2] = verb
        for i in range(0, len(data), 4):
            try:
                if not OPCODES[data[i]](i + 1, i + 2, i + 3):
                    break
            except KeyError:
                break

def pairs():
    global noun, verb
    for noun in range(0, 100):
        for verb in range(0, 100):
            yield noun, verb

def add(*argv):
    global data
    data[data[argv[2]]] = data[data[argv[0]]] + data[data[argv[1]]]
    return True

def multiply(*argv):
    global data
    data[data[argv[2]]] = data[data[argv[0]]] * data[data[argv[1]]]
    return True

def finish(*argv):
    global data, noun, verb
    if data[0] == 19690720:
        print(100 * noun + verb)
        raise SystemExit
    return False

OPCODES = {
    1: add,
    2: multiply,
    99: finish
}

def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read().split(",")]

if __name__ == "__main__":
    main()