import itertools
import math
import numpy as np

def main():
    paths = {}
    asteroids = []
    _map = read()
    for h in range(0, len(_map)):
        for w in range(0, len(_map[h])):
            if _map[h][w] == "#":
                asteroids.append((w, h))

    #print(asteroids)
    origin = (5,8)
    _list = [a for a in asteroids if a != origin]
    origin = (0,0)
    #print(_list)
    #return
    for point in _list:
        point = (point[0] - 5, point[1] - 8)
        #print(str(origin[::1]) + " to " + str(point[::1]))

        slope = math.degrees(math.atan2((point[1] - origin[1]), (point[0] - origin[0])))
        ang1 = np.arctan2(*origin[::-1])
        print(ang1)
        ang2 = np.arctan2(*point[::-1])
        print(ang2)            
        print(str(origin[::1]) + " to " + str(point[::1]) + ": " + str(slope) + " - " + str(np.rad2deg((ang1 - ang2) % (2 * np.pi))))
        dot = point[0] * origin[0] + point[1] * origin[1]
        det = point[1] * origin[0] - point[0] * origin[1]
        angle = math.atan2(det, dot)
        print("Angle: " + str(np.rad2deg(angle % (2 * np.pi))))

        continue

        if not a in paths:
            paths[a] = {}
        slope = math.degrees(math.atan2((b[1] - a[1]), (b[0] - a[0])))
        paths[a][slope] = True

        if a == (5,8):
            ang1 = np.arctan2(*b[::-1])
            print(ang1)
            ang2 = np.arctan2(*a[::-1])
            print(ang2)
            print(str(b[::1]) + " to " + str(a[::1]) + ": " + str(slope) + " - " + str(np.rad2deg((ang1 - ang2) % (2 * np.pi))))

        if not b in paths:
            paths[b] = {}
        slope = math.degrees(math.atan2((a[1] - b[1]), (a[0] - b[0])))
        paths[b][slope] = True

        if b == (5,8):
            ang1 = np.arctan2(*a[::-1])
            print(ang1)
            ang2 = np.arctan2(*b[::-1])
            print(ang2)            
            print(str(a[::1]) + " to " + str(b[::1]) + ": " + str(slope) + " - " + str(np.rad2deg((ang1 - ang2) % (2 * np.pi))))
            dot = b[0] * a[0] + b[1] * a[1]
            det = b[1] * a[0] - b[0] * a[1]
            angle = math.atan2(det, dot)
            print("Angle: " + str(np.rad2deg(angle % (2 * np.pi))))
    
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