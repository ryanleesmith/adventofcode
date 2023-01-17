class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = {}
        self.files = []

    def addDir(self, dir):
        self.dirs[dir.name] = dir

    def getDir(self, name):
        return self.dirs[name]

    def addFile(self, file):
        self.files.append(file)

    def calcSize(self):
        size = 0
        for file in self.files:
            size = size + file.size
        for dir in self.dirs.values():
            size = size + dir.calcSize()
        return size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def main():
    commands = read()
    root = Dir("/", None)
    dirs = [root]
    currDir = root
    for command in commands[1:]:
        if command.startswith("$ cd"):
            if command[5:] == "..":
                currDir = currDir.parent
            else:
                currDir = currDir.getDir(command[5:])
        elif command.startswith("dir"):
            dir = Dir(command[4:], currDir)
            dirs.append(dir)
            currDir.addDir(dir)
        elif not command.startswith("$"):
            details = command.split(" ")
            file = File(details[1], int(details[0]))
            currDir.addFile(file)

    total = 0
    for dir in dirs:
        size = dir.calcSize()
        if size <= 100000:
            total = total + size
    print(total)

def read():
    return open("input.txt", "r").read().splitlines()

if __name__ == "__main__":
    main()
