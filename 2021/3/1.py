def main():
    data = read()
    len = 12
    gamma = []
    epsilon = []
    for i in range(0, len):
        zeroes = 0
        ones = 0
        for line in data:
            if int(line[i]) == 0:
                zeroes = zeroes + 1
            else:
                ones = ones + 1
        if zeroes > ones:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)
    print(toBinary(gamma) * toBinary(epsilon))

def toBinary(input):
    sum = 0
    input = input[::-1]
    for i in range(len(input) - 1, -1, -1):
        if input[i]:
            sum = sum + 2 ** i
    return sum

def read():
    input = open("input.txt", "r")
    return [line.split()[0] for line in input.read().splitlines()]

if __name__ == "__main__":
    main()
