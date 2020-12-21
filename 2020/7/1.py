import re
SHINY_GOLD = 'shiny gold'
bags = {}

class Bag:
    def __init__(self, data):
        self.color = data[0]
        self.bags = []
        map(lambda childBag: addChild(self, childBag.strip()), data[1].split(","))

    def hasGold(self):
        if self.color == SHINY_GOLD:
            return True
        elif len(self.bags) == 0:
            return False
        else:
            return len(filter(lambda bag: getBag(bag).hasGold(), self.bags)) > 0

def getBag(bag):
    return bags[bag]

def main():
    global bags
    input = open("input.txt", "r")
    map(lambda line: parseLine(line), input.read().splitlines())
    print(sum(map(lambda bag: bag.color != SHINY_GOLD and bag.hasGold(), bags.values())))

def parseLine(line):
    global bags
    tuples = re.findall("([a-z\ ]+) bags contain (.+).", line)
    bag = [Bag(bag) for bag in tuples][0]
    bags[bag.color] = bag

def addChild(bag, childBag):
    if childBag == "no other bags":
        return
    tuples = re.findall("[\d+] (.+) bags?", childBag)
    bag.bags.append([bag for bag in tuples][0])

if __name__ == "__main__":
    main()
