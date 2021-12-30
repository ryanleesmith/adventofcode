def main():
    o2rating = read()
    co2rating = read()
    for idx in range(0, 12):
        o2rating = o2(idx, o2rating)
        if len(o2rating) == 1:
            break
    for idx in range(0, 12):
        co2rating = co2(idx, co2rating)
        if len(co2rating) == 1:
            break
    print(toBinary([int(i) for i in o2rating[0]]) * toBinary([int(i) for i in co2rating[0]]))

def o2(idx, data):
    zeroes = 0
    ones = 0
    for line in data:
        if int(line[idx]) == 0:
            zeroes = zeroes + 1
        else:
            ones = ones + 1
    if zeroes > ones:
        o2 = 0
    else:
        o2 = 1
    scrubbed = []
    for line in data:
        if int(line[idx]) == o2:
            scrubbed.append(line)
    return scrubbed

def co2(idx, data):
    zeroes = 0
    ones = 0
    for line in data:
        if int(line[idx]) == 0:
            zeroes = zeroes + 1
        else:
            ones = ones + 1
    if zeroes <= ones:
        co2 = 0
    else:
        co2 = 1
    scrubbed = []
    for line in data:
        if int(line[idx]) == co2:
            scrubbed.append(line)
    return scrubbed

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
