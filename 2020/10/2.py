from functools import reduce
import math

def main():
    input = open("input.txt", "r")
    adapters = sorted([int(line) for line in input.read().splitlines()])
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters = sorted(adapters)

    total = 0
    paths = []
    for i in range(len(adapters) - 2):
        count = 0
        if i + 4 < len(adapters) and adapters[i + 4] - adapters[i] == 4:
            if adapters[i + 4] - adapters[i - 3] != 1:
                count = 7
        elif i + 3 < len(adapters) and adapters[i + 3] - adapters[i] == 3:
            if adapters[i + 3] - adapters[i - 1] != 4:
                count = 4
        elif i + 2 < len(adapters) and adapters[i + 2] - adapters[i] == 2:
            if adapters[i + 2] - adapters[i - 1] != 3:
                count = 2
        if count != 0:
            paths.append(count)

    total = reduce(lambda x, y: x*y, paths)
    print(total)

if __name__ == "__main__":
    main()
