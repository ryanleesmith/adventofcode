def main():
    outputs = read()
    count = 0
    for output in outputs:
        count = count + len(filter(lambda i: len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7, output))
    print(count)

def read():
    input = open("input.txt", "r")
    return [[output for output in output.split()] for (signals, output) in list(line.split(" | ") for line in input.read().splitlines())]

if __name__ == "__main__":
    main()
