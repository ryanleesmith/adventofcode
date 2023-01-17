def main():
    rucksacks = read()
    matches = []
    groups = []
    for rucksack in rucksacks:
        groups.append(rucksack)
        if len(groups) == 3:
            matches.append(list(set(convert(groups[0])) & set(convert(groups[1])) & set(convert(groups[2])))[0])
            groups = []
    print(sum(matches))

def convert(rucksack):
    return map(lambda i: ord(i) - 96 if ord(i) > 96 else ord(i) - 38, rucksack)

def read():
    input = open("input.txt", "r")
    return [[i for i in list(line)] for line in input.read().splitlines()]

if __name__ == "__main__":
    main()
