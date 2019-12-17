reactions = {}
chemicals = {"FUEL": 0}
ore = 0

class Chemical:
    def __init__(self, info):
        info = info.split(" ")
        self.qty = int(info[0])
        self.name = info[1]

    def make(self):
        global reactions, chemicals, ore
        if self.name == "ORE":
            #print(str(self.qty) + " " + self.name)
            ore += self.qty
        elif self.name in chemicals and chemicals[self.name] >= self.qty:
            chemicals[self.name] -= self.qty
            #print("Found: " + self.name + ", " + str(chemicals[self.name]) + " left")
        else:
            #print("Find reaction for: " + str(self.qty) + " " + self.name)
            reactions[self.name].make()

class Reaction:
    def __init__(self, _in, _out):
        self._in = _in
        self._out = _out

    def make(self):
        #print("Make: " + str(self._out.qty) + " " + self._out.name)
        for chemical in self._in:
            #print("Need: " + str(chemical.qty) + " " + chemical.name)
            if chemical.name == "ORE":
                chemical.make()
            else:
                while chemicals[chemical.name] < chemical.qty:
                    chemical.make()
                chemicals[chemical.name] -= chemical.qty
        if self._out.name != "FUEL":
            chemicals[self._out.name] += self._out.qty
            #print("Store " + str(chemicals[self._out.name]) + " " + self._out.name)

def main():
    global reactions, chemicals

    data = read()
    for line in data:
        _in = list(map(lambda i: Chemical(i.strip()), line[0].split(",")))
        _out = Chemical(line[1].strip())
        reactions[_out.name] = Reaction(_in, _out)
        for chemical in _in:
            chemicals[chemical.name] = 0

    reactions["FUEL"].make()
    print("Needed " + str(ore) + " ORE")
    print(chemicals)

def read():
    _input = open("input.txt", "r")
    return [str(i).split("=>") for i in _input.read().splitlines()]

if __name__ == "__main__":
    main()