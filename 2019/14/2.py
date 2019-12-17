import math

reactions = {}
chemicals = {"FUEL": 0}
ore = 0

class Chemical:
    def __init__(self, info):
        info = info.split(" ")
        self.qty = float(info[0])
        self.name = info[1]

    def make(self, qty):
        global reactions, chemicals, ore
        if self.name == "ORE":
            #print("Making " + str(self.qty * qty) + " ORE")
            ore += self.qty * qty
        else:
            #print("Reaction for: " + self.name)
            reactions[self.name].make(qty)

class Reaction:
    def __init__(self, _in, _out):
        self._in = _in
        self._out = _out

    def make(self, qty):
        #print("Make: " + str(self._out.qty) + " " + self._out.name)
        for chemical in self._in:
            #print("Need: " + str(chemical.qty) + " " + chemical.name)
            if chemical.name == "ORE":
                chemical.make(qty)
            else:
                #print("Ratio: " + str(chemical.qty) + "/" + str(reactions[chemical.name]._out.qty))
                #print(str(chemicals[chemical.name]) + " exists")
                ratio = chemical.qty / reactions[chemical.name]._out.qty
                ratio = 1
                while chemicals[chemical.name] < chemical.qty:
                    chemical.make(ratio)
                chemicals[chemical.name] -= chemical.qty

        chemicals[self._out.name] += self._out.qty * qty

def main():
    global reactions, chemicals

    data = read()
    for line in data:
        _in = list(map(lambda i: Chemical(i.strip()), line[0].split(",")))
        _out = Chemical(line[1].strip())

        fuel = 1
        for chemical in _in:
            #if chemical.name != "ORE":
                chemical.qty = chemical.qty * fuel
        #if _out.name != "FUEL":# and _in[0].name != "ORE":
        _out.qty = _out.qty * fuel

        reactions[_out.name] = Reaction(_in, _out)
        for chemical in _in:
            chemicals[chemical.name] = 0

    leftover = False
    while not leftover:
        leftover = True
        reactions["FUEL"].make(1)
        for chemical in chemicals:
            if chemical != "FUEL" and chemical != "ORE":
                if chemicals[chemical] > 0:
                    leftover = False
        
    print("Needed " + str(ore) + " ORE")
    print(chemicals)
    
    print(str(math.floor((1000000000000 / ore) * chemicals["FUEL"])))

def read():
    _input = open("input.txt", "r")
    return [str(i).split("=>") for i in _input.read().splitlines()]

if __name__ == "__main__":
    main()