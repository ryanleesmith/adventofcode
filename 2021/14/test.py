from collections import Counter

def main():
    template, rules = read()
    print template
    print rules
    polymer = []
    for idx in range(len(template) - 1):
        polymer.append(''.join(template[idx:idx+2]))

    for idx in range(40):
        print idx
        tmp_polymer = polymer[:]
        idx_bump = 0
        for idx, entry in enumerate(polymer):
            if rules.has_key(entry):
                tmp_polymer[idx + idx_bump] = polymer[idx][0] + rules[entry]
                tmp_polymer.insert(idx + 1 + idx_bump, rules[entry] + polymer[idx][1])
                idx_bump = idx_bump + 1
        polymer = tmp_polymer

    output = ''
    for idx, entry in enumerate(polymer):
        if idx < len(polymer) - 1:
            output = output + entry[0]
        else:
            output = output + entry
    #print polymer
    #print output
    values = dict(Counter(output))
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
