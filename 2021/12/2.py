count = 0

class Cave:
    def __init__(self, name):
        self.name = name
        self.start = None
        self.end = None
        self.points = []

    def addPoint(self, cave):
        self.points.append(cave)

    def isStart(self):
        return self.name == "start"

    def isEnd(self):
        return self.name == "end"
    
    def isSmall(self):
        return self.name.islower()

def traverse(cave, path, hitSmall):
    global count
    if (len(path) > 0 and cave.isStart()):
        return False
    if cave.isSmall() and cave in path:
        if hitSmall:
            return False
        else:
            hitSmall = True
    path.append(cave)
    if cave.isEnd():
        return True
    for cave in cave.points:
        newPath = path[:]
        if traverse(cave, newPath, hitSmall):
            count = count + 1

def main():
    global count
    start = None
    caves = {}
    for (left, right) in list(read()):
        left = Cave(left) if not caves.has_key(left) else caves[left]
        right = Cave(right) if not caves.has_key(right) else caves[right]
        left.addPoint(right)
        right.addPoint(left)
        if (left.isStart() or right.isStart()) and start == None:
            start = left if left.isStart() else right
        caves[left.name] = left
        caves[right.name] = right
    traverse(start, [], False)
    print(count)

def read():
    input = open("input.txt", "r")
    return [[left, right] for (left, right) in list(line.split("-") for line in input.read().splitlines())]

if __name__ == "__main__":
    main()
