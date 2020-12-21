import re
SHINY_GOLD = 'shiny gold'
bags = {}

class Bag:
    def __init__(self, data):
        self.color = data[0]
        self.bags = {}
        map(lambda childBag: addChild(self, childBag.strip()), data[1].split(","))
    
    def count(self):
        return sum(map(lambda child: child[1] + (child[1] * getBag(child[0]).count()), self.bags.items()))


def getBag(bag):
    return bags[bag]

def main():
    global bags
    input = open("input.txt", "r")
    map(lambda line: parseLine(line), input.read().splitlines())
    print(getBag(SHINY_GOLD).count())

def parseLine(line):
    global bags
    tuples = re.findall("([a-z\ ]+) bags contain (.+).", line)
    bag = [Bag(bag) for bag in tuples][0]
    bags[bag.color] = bag

def addChild(bag, childBag):
    if childBag == "no other bags":
        return
    tuples = re.findall("([\d+]) (.+) bags?", childBag)
    pair = [entry for entry in tuples][0]
    bag.bags[pair[1]] = int(pair[0])

if __name__ == "__main__":
    main()
