import re

def main():
    sensors, beacons = read()
    print(sensors)
    print(beacons)

def read():
    input = open("input.txt", "r")
    sensors = []
    beacons = []
    for group in [[i for i in line.split(": ")] for line in input.read().splitlines()]:
        sensors.append([int(i) for i in re.findall( r'(-?\d+)', group[0])])
        beacons.append([int(i) for i in re.findall( r'(-?\d+)', group[1])])
    return sensors, beacons

if __name__ == "__main__":
    main()
