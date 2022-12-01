from collections import Counter

def main():
    template, rules = read()
    for i in range(1, 11):
        template = insert(template, rules)
    values = dict(Counter(template))
    minElement = None
    maxElement = 0
    for value in values.values():
        minElement = value if minElement == None else min(minElement, value)
        maxElement = max(maxElement, value)
    print(maxElement - minElement)

def insert(template, rules):
    splitTemplate = []
    inserted = []
    for idx, char in enumerate(template):
        if idx < len(template) - 1:
            splitTemplate.append(char + template[idx + 1])
    for idx, chunk in enumerate(splitTemplate):
        if rules.has_key(chunk):
            template.insert(idx + 1 + len(filter(lambda i: i < idx, inserted)), rules[chunk])
            inserted.append(idx)
    return template

def read():
    input = open("input.txt", "r")
    template, rules = [lines for (lines) in list(line.splitlines() for line in input.read().split("\n\n"))]
    template = list(template[0])
    rules = [[i for i in rule.split(' -> ')] for rule in rules]
    keyedRules = {}
    for rule in rules:
        keyedRules[rule[0]] = rule[1]
    return template, keyedRules

if __name__ == "__main__":
    main()
