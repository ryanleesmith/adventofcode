def main():
    program = read()
    cycle = 0
    x = 1
    output = ""
    for line in program:
        cycle = cycle + 1
        if cycle - 1 in range(x - 1, x + 2):
            output = output + "#"
        else:
            output = output + " "
        if cycle == 40:
            output = output + "\r\n"
            cycle = 0
        if line[0] == "addx":
            cycle = cycle + 1
            if cycle - 1 in range(x - 1, x + 2):
                output = output + "#"
            else:
                output = output + " "
            if cycle == 40:
                output = output + "\r\n"
                cycle = 0
            x = x + line[1]
    print(output)

def read():
    input = open("input.txt", "r")
    return [[inst, int(val[0]) if len(val) == 1 else None] for (inst, *val) in list(line.split(" ") for line in input.read().splitlines())]

if __name__ == "__main__":
    main()
