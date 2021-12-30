def main():
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    points = [3, 57, 1197, 25137]
    lines = read()
    score = 0
    for line in lines:
        opened = []
        for char in line:
            if char in openers:
                opened.append(char)
            elif char in closers:
                index = closers.index(char)
                if opened[-1] == openers[index]:
                    opened.pop()
                else:
                    score = score + points[index]
                    break
    print(score)

def read():
    input = open("input.txt", "r")
    return [[str(i) for i in list(line)] for line in input.read().splitlines()]

if __name__ == "__main__":
    main()
