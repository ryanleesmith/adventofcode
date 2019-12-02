import math

def main():
    total = 0
    data = read()
    for mass in data:
        total += calc(mass)
    print(total)

def read():
    data = []
    input = open("input.txt", "r")
    for line in input.read().splitlines():
        data.append(int(line))
    return data

def calc(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    fuel += calc(fuel)
    return fuel

if __name__ == "__main__":
    main()