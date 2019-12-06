import sys

class Node:
    def __init__(self, orbit, parent, orbits):
        self.orbit = orbit
        self.parent = parent
        self.children = []
        self.insert(orbits)

    def insert(self, orbits):
        for orbit in dict(filter(lambda elem: elem[1] == self.orbit, orbits.items())):
            self.children.append(Node(orbit, self, orbits))
        return
    
    def get_orbit(self, orbit):
        if self.orbit == orbit:
            return self.parent
        else:
            for child in self.children:
                _orbit = child.get_orbit(orbit)
                if _orbit is not None:
                    return _orbit
        

def main():
    sys.setrecursionlimit(10000)
    orbits = read()
    root = Node("COM", None, orbits)

    you_list = []
    orbit = root.get_orbit("YOU")
    while orbit != None:
        you_list.append(orbit.orbit)
        orbit = root.get_orbit(orbit.orbit)

    san_list = []
    orbit = root.get_orbit("SAN")
    while orbit != None:
        san_list.append(orbit.orbit)
        orbit = root.get_orbit(orbit.orbit)

    you_hop = -1
    for x in you_list:
        you_hop += 1
        san_hop = -1
        for y in san_list:
            san_hop += 1
            if x == y:
                print(you_hop + san_hop)
                break
        else:
            continue
        break

def read():
    data = []
    input = open("input.txt", "r")
    return {j[1]: j[0] for j in [i.split(")") for i in input.read().splitlines()]}

if __name__ == "__main__":
    main()