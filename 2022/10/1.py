def main():
    program = read()
    cycle = 0
    x = 1
    strength = 0
    for line in program:
        cycle = cycle + 1
        if (cycle - 20) % 40 == 0:
            strength = strength + (cycle  * x)
        if line[0] == "addx":
            cycle = cycle + 1
            if (cycle - 20) % 40 == 0:
                strength = strength + (cycle  * x)
            x = x + line[1]
    print(strength)

def read():
    input = open("input.txt", "r")
    return [[inst, int(val[0]) if len(val) == 1 else None] for (inst, *val) in list(line.split(" ") for line in input.read().splitlines())]

if __name__ == "__main__":
    main()
