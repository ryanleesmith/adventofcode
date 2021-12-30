def main():
    data = read()
    total = 0

    for row in data:
        mapped = {}
        config = {}
        display = {}

        for known in filter(lambda i: len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7, row[0]):
            if len(known) == 2:
                mapped[known] = 1
                config[1] = known
            elif len(known) == 3:
                mapped[known] = 7
                config[7] = known
            elif len(known) == 4:
                mapped[known] = 4
                config[4] = known
            elif len(known) == 7:
                mapped[known] = 8
                config[8] = known

        side = config[1]

        tmp = config[7]
        for i in list(config[1]):
            tmp = tmp.replace(i, "")
        display[0] = tmp

        tmp = config[4]
        for i in list(config[1]):
            tmp = tmp.replace(i, "")
        upper = tmp

        tmp = config[8]
        for i in list(config[4]):
            tmp = tmp.replace(i, "")
        lower = tmp.replace(display[0], "")

        for known in filter(lambda i: len(i) == 5, row[0]):
            if all(elem in list(known) for elem in list(side)):
                mapped[known] = 3
                config[3] = known

        for known in filter(lambda i: len(i) == 5 and i != config[3], row[0]):
            if all(elem in list(known) for elem in list(upper)):
                mapped[known] = 5
                config[5] = known
            elif all(elem in list(known) for elem in list(lower)):
                mapped[known] = 2
                config[2] = known

        for elem in side:
            if elem in list(config[2]):
                display[2] = elem
            elif elem in list(config[5]):
                display[5] = elem

        for elem in upper:
            if elem not in list(config[2]):
                display[1] = elem
                display[3] = upper.replace(elem, "")

        for elem in lower:
            if elem not in list(config[3]):
                display[4] = elem
                display[6] = lower.replace(elem, "")

        zero = display[0] + display[1] + display[2] + display[4] + display[5] + display[6]
        for known in filter(lambda i: len(i) == 6, row[0]):
            if all(elem in list(known) for elem in list(zero)):
                mapped[known] = 0
                config[0] = known

        six = display[0] + display[1] + display[3] + display[4] + display[5] + display[6]
        for known in filter(lambda i: len(i) == 6, row[0]):
            if all(elem in list(known) for elem in list(six)):
                mapped[known] = 6
                config[6] = known

        nine = display[0] + display[1] + display[2] + display[3] + display[5] + display[6]
        for known in filter(lambda i: len(i) == 6, row[0]):
            if all(elem in list(known) for elem in list(nine)):
                mapped[known] = 9
                config[9] = known

        num = ""
        for i in row[1]:
            for value in filter(lambda value: len(value) == len(i), mapped.keys()):
                if all(elem in list(i) for elem in list(value)):
                    num = num + str(mapped[value])
        total = total + int(num)
    print(total)

def read():
    input = open("input.txt", "r")
    return [[[i for i in signals.split()], [i for i in output.split()]] for (signals, output) in list(line.split(" | ") for line in input.read().splitlines())]

if __name__ == "__main__":
    main()
