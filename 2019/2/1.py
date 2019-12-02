data = []

def main():
    global data
    data = read()
    data[1] = 12
    data[2] = 2
    for i in range(0, len(data), 4):
        OPCODES[data[i]](i + 1, i + 2, i + 3)

def add(*argv):
    global data
    data[data[argv[2]]] = data[data[argv[0]]] + data[data[argv[1]]]

def multiply(*argv):
    global data
    data[data[argv[2]]] = data[data[argv[0]]] * data[data[argv[1]]]

def finish(*argv):
    global data
    print(data[0])
    raise SystemExit

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