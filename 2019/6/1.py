import sys

class Node:
    def __init__(self, orbit, orbits):
        self.orbit = orbit
        self.children = []
        self.insert(orbits)

    def insert(self, orbits):
        for orbit in dict(filter(lambda elem: elem[1] == self.orbit, orbits.items())):
            self.children.append(Node(orbit, orbits))
        return

    def count(self, nest):
        total = 0
        for child in self.children:
            total += nest
            total += child.count(nest + 1)
        return total
        

def main():
    sys.setrecursionlimit(10000)
    orbits = read()
    root = Node("COM", orbits)
    print(root.count(1))
    return

def read():
    data = []
    input = open("input.txt", "r")
    return {j[1]: j[0] for j in [i.split(")") for i in input.read().splitlines()]}

if __name__ == "__main__":
    main()