import itertools
import math

def main():
    paths = {}
    asteroids = []
    _map = read()
    for h in range(0, len(_map)):
        for w in range(0, len(_map[h])):
            if _map[h][w] == "#":
                asteroids.append((w, h))

    for a, b in itertools.combinations(asteroids, 2):
        if not a in paths:
            paths[a] = {}
        try:
            slope = math.degrees(math.atan2((b[1] - a[1]), (b[0] - a[0])))
        except ZeroDivisionError:
            slope = None
            if a[1] > b[1]:
                slope = "-None"
        paths[a][slope] = True

        if not b in paths:
            paths[b] = {}
        try:
            slope = math.degrees(math.atan2((a[1] - b[1]), (a[0] - b[0])))
        except ZeroDivisionError:
            slope = None
            if b[1] > a[1]:
                slope = "-None"
        paths[b][slope] = True
    
    _path = None
    _max = 0
    for path in paths:
        if len(paths[path]) > _max:
            _max = len(paths[path])
            _path = path
            
    print(str(_path) + ": " + str(len(paths[_path])))

def read():
    input = open("input.txt", "r")
    return [[*str(i)] for i in input.read().splitlines()]

if __name__ == "__main__":
    main()