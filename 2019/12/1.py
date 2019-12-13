from itertools import permutations

class Moon:
    def __init__(self, pos):
        self.pos = [int(i) for i in pos]
        self.vel = [0,0,0]

def main():
    moons = []
    data = read()
    for pos in data:
        moons.append(Moon(pos))
    
    for _ in range(1000):
        for moon in moons:
            for other in moons:
                if other != moon:
                    for i in range(3):
                        if other.pos[i] > moon.pos[i]:
                            moon.vel[i] += 1
                        elif other.pos[i] < moon.pos[i]:
                            moon.vel[i] -= 1
        
        energy = 0
        for moon in moons:
            pot = 0
            kit = 0
            for i in range(3):
                moon.pos[i] += moon.vel[i]
                pot += abs(moon.pos[i])
                kit += abs(moon.vel[i])
            energy += pot * kit

        print(energy)

def read():
    _input = open("input.txt", "r")
    return [[*str(i).split(",")] for i in _input.read().splitlines()]

if __name__ == "__main__":
    main()