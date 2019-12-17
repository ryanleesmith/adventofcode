import math

reactions = {}
demand = {}
supply = {"FUEL": 0}
ore = 0

class Chemical:
    def __init__(self, info):
        info = info.split(" ")
        self.qty = int(info[0])
        self.name = info[1]

    def make(self, qty):
        global reactions, ore
        if self.name == "ORE":
            ore += self.qty * qty
        else:
            reactions[self.name].make(qty)

class Reaction:
    def __init__(self, _in, _out):
        self._in = _in
        self._out = _out

    def make(self, qty):
        for chemical in self._in:
            ratio = math.ceil(qty / self._out.qty)
            if chemical.name == "ORE":
                chemical.make(ratio)
            else:
                ratio = math.ceil(qty / self._out.qty) * chemical.qty - supply[chemical.name]
                while supply[chemical.name] < ratio:
                    chemical.make(ratio)
                supply[chemical.name] -= ratio

        supply[self._out.name] += math.ceil((qty / self._out.qty)) * self._out.qty

def main():
    global reactions, supply

    data = read()
    for line in data:
        _in = list(map(lambda i: Chemical(i.strip()), line[0].split(",")))
        _out = Chemical(line[1].strip())

        reactions[_out.name] = Reaction(_in, _out)
        for chemical in _in:
            supply[chemical.name] = 0
    
    reactions["FUEL"].make(1)
        
    print("Needed " + str(ore) + " ORE")
    print(supply)

def read():
    _input = open("input.txt", "r")
    return [str(i).split("=>") for i in _input.read().splitlines()]

if __name__ == "__main__":
    main()