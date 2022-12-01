def main():
    elves = read()
    total = list(map(lambda calories: sum(calories), elves))
    total.sort(reverse=True)
    print(total[0])

def read():
    input = open("input.txt", "r")
    return [[int(i) for i in line.splitlines()] for line in input.read().split("\n\n")]

if __name__ == "__main__":
    main()
