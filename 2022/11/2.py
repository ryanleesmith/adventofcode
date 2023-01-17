import math, heapq

monkeys = []

class Monkey:
    def __init__(self, monkey):
        self.name = monkey[0][-2]
        self.items = [int(i) for i in monkey[1][18:].split(", ")]
        self.operation = monkey[2][19:]
        self.divisor = int(monkey[3][21:])
        self.decision = [int(monkey[5][-1]), int(monkey[4][-1])]
        self.inspectionCount = 0

    def inspect(self):
        global monkeys
        for item in self.items:
            self.inspectionCount = self.inspectionCount + 1
            item = eval(self.operation, {}, {"old": item})
            monkeys[self.decision[item % self.divisor == 0]].items.append(item)
        self.items = []

    def __str__(self):
        return "Monkey {}: {}".format(self.name, self.inspectionCount)

def main():
    data = read()
    for monkey in data:
        monkeys.append(Monkey(monkey))
    prev = None
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect()
        #monkey = max(monkeys, key = lambda monkey: monkey.inspectionCount)
        curr = monkeys[0].inspectionCount
        if prev != None:
            print(curr - prev)
        prev = curr
    top = heapq.nlargest(2, monkeys, lambda monkey: monkey.inspectionCount)
    print(top[0].inspectionCount * top[1].inspectionCount)

def read():
    input = open("input.txt", "r")
    return [[i for i in line.splitlines()] for line in input.read().split("\n\n")]

if __name__ == "__main__":
    main()
