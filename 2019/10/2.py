import itertools
import math
import numpy as np

def get_asteroids():
    asteroids = []
    _map = read()
    for h in range(0, len(_map)):
        for w in range(0, len(_map[h])):
            if _map[h][w] == "#":
                asteroids.append((w, h))
    return asteroids

def get_angle(_from, _to):
    origin = (0,0)
    point = (_to[0] - _from[0], _to[1] - _from[1])
    return round(np.rad2deg((np.arctan2(*origin[::-1]) - np.arctan2(*point[::-1])) % (2 * np.pi)), 2)

def get_optimal_origin(asteroids):
    paths = {}
    origin = (0,0)
    for a, b in itertools.combinations(asteroids, 2):
        if not a in paths:
            paths[a] = {}

        angle = get_angle(a, b)
        paths[a][angle] = True

        if not b in paths:
            paths[b] = {}
        
        angle = get_angle(b, a)
        paths[b][angle] = True
    
    _path = None
    _max = 0
    for path in paths:
        if len(paths[path]) > _max:
            _max = len(paths[path])
            _path = path
            
    print(str(_path) + ": " + str(len(paths[_path])))
    return _path

def get_distance(_from, _to):
    return abs(_to[0] - _from[0]) + abs(_to[1] - _from[1])

class Asteroid:
    def __init__(self, point, distance):
        self.point = point
        self.distance = distance

def main():
    asteroids = get_asteroids()
    origin = get_optimal_origin(asteroids)

    paths = {}
    _list = [a for a in asteroids if a != origin]
    for point in _list:
        angle = get_angle(origin, point)
        distance = get_distance(origin, point)
        if not angle in paths:
            paths[angle] = []
        paths[angle].append(Asteroid(point[::1], distance))
    
    for path in paths:
        paths[path].sort(key=lambda asteroid: asteroid.distance)

    destroyed = 0
    asteroid = None
    while destroyed < 201:
        for degree in range(36000, -1, -1):
            degree = round(np.rad2deg((np.deg2rad(degree / 100) + np.deg2rad(90)) % (2 * np.pi)), 2)
            if degree in paths:
                asteroid = paths[degree].pop(0)
                destroyed += 1
                if destroyed == 200:
                    print("Destroyed " + str(destroyed) + ": " + str(asteroid.point))

def read():
    input = open("input.txt", "r")
    return [[*str(i)] for i in input.read().splitlines()]

if __name__ == "__main__":
    main()