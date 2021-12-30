def main():
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    points = [1, 2, 3, 4]
    lines = read()
    scores = []
    for line in lines:
        score = 0
        opened = []
        for char in line:
            if char in openers:
                opened.append(char)
            elif char in closers:
                index = closers.index(char)
                if opened[-1] == openers[index]:
                    opened.pop()
                else:
                    break
        else:
            for idx in range(len(opened) - 1, -1, -1):
                score = (score * 5) + points[openers.index(opened[idx])]
            scores.append(score)
    scores.sort()
    print(scores[len(scores) / 2])

def read():
    input = open("input.txt", "r")
    return [[str(i) for i in list(line)] for line in input.read().splitlines()]

if __name__ == "__main__":
    main()
