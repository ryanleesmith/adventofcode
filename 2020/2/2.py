import re

class Password:
    def __init__(self, data):
        self.pos1 = int(data[0])
        self.pos2 = int(data[1])
        self.letter = data[2]
        self.password = data[3]

    def isValid(self):
        return bool(self.password[self.pos1-1] == self.letter) ^ (self.password[self.pos2-1] == self.letter)

def main():
    print(sum(map(lambda x: x.isValid(), read())))

def read():
    data = []
    input = open("input.txt", "r")
    for line in input.read().splitlines():
        tuples = re.findall("(\d+)-(\d+) ([a-z]): ([a-z]+)", line)
        data.append([Password(entry) for entry in tuples][0])
    return data

if __name__ == "__main__":
    main()
