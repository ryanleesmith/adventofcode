import math
from numpy import mean

def main():
    positions = read()
    mn = int(math.floor(mean(positions)))
    fuel = 0
    for pos in positions:
        fuel = fuel + sum(map(lambda x: x + 1, range(0,abs(pos - mn))))
    print(fuel)

def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read().split(",")]

if __name__ == "__main__":
    main()
