def main():
    assignments = read()
    overlaps = 0
    for assignment in assignments:
        first = list(dict.fromkeys(list(range(assignment[0][0], assignment[0][1] + 1))))
        second = list(dict.fromkeys(list(range(assignment[1][0], assignment[1][1] + 1))))
        if any(x in first for x in second) or any(x in second for x in first):
            overlaps = overlaps + 1
    print(overlaps)

def read():
    input = open("input.txt", "r")
    return [[[int(section) for section in i.split("-")] for i in line.split(",")] for line in input.read().splitlines()]

if __name__ == "__main__":
    main()
