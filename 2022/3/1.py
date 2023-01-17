def main():
    data = read()
    rucksacks = [(i[0:len(i)/2], i[len(i)/2:len(i)]) for i in data]
    matches = []
    for rucksack in rucksacks:
        matches.append(list(set(convert(rucksack[0])) & set(convert(rucksack[1])))[0])
    print(sum(matches))

def convert(rucksack):
    return map(lambda i: ord(i) - 96 if ord(i) > 96 else ord(i) - 38, rucksack)

def read():
    input = open("input.txt", "r")
    return [[i for i in list(line)] for line in input.read().splitlines()]

if __name__ == "__main__":
    main()
