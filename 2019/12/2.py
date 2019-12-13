from itertools import permutations
from os import system
import numpy as np

class Moon:
    def __init__(self, pos):
        self.orig = [int(i) for i in pos]
        self.pos = [int(i) for i in pos]
        self.vel = [0,0,0]

def adjust(moon, other, axis):
    if other.pos[axis] > moon.pos[axis]:
        moon.vel[axis] += 1
    elif other.pos[axis] < moon.pos[axis]:
        moon.vel[axis] -= 1

def move(moon, axis):
    moon.pos[axis] += moon.vel[axis]

def main():
    moons = []
    data = read()
    for pos in data:
        moons.append(Moon(pos))
    
    steps = 0

    cycle = [None, None, None]

    while any(cycle is None for cycle in cycle):
        steps += 1
        
        for moon in moons:
            for other in moons:
                if other != moon:
                    for i in range(3):
                        adjust(moon, other, i)
        
        axis = [True, True, True]
        for moon in moons:
            for i in range(3):
                move(moon, i)
                if moon.pos[i] != moon.orig[i] or moon.vel[i] != 0:
                    axis[i] = False

        for i in range(3):
            if axis[i] and cycle[i] is None:
                cycle[i] = steps
    
    print(np.lcm.reduce(cycle))

def read():
    _input = open("input.txt", "r")
    return [[*str(i).split(",")] for i in _input.read().splitlines()]

if __name__ == "__main__":
    main()