PREAMBLE = 25
data = []

def main():
    input = open("input.txt", "r")
    data = [int(line) for line in input.read().splitlines()]
    for i in range(PREAMBLE, len(data)):
        found = False
        pairs = data[i - PREAMBLE:PREAMBLE + i]
        for x in range(PREAMBLE):
            for y in range(x + 1, PREAMBLE):
                if pairs[x] + pairs[y] == data[i]:
                    found = True
        if not found:
            print(data[i])

if __name__ == "__main__":
    main()
