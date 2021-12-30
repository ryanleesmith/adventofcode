from numpy import median

def main():
    positions = read()
    med = int(median(positions))
    fuel = 0
    for pos in positions:
        fuel = fuel + abs(pos - med)
    print(fuel)

def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read().split(",")]

if __name__ == "__main__":
    main()
