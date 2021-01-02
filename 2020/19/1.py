import re

def main():
    rules = {}
    input = open("input.txt", "r")
    (input_rules, input_messages) = input.read().split("\n\n")

    input_rules = input_rules.splitlines()
    while len(rules) < len(input_rules):
        for input_rule in input_rules:
            (rule, expr) = input_rule.split(": ")
            if expr == '"a"' or expr == '"b"':
                rules[rule] = expr[1]
            else:
                found = True
                built = []
                for block in expr.split(" | "):
                    pointers = block.split(" ")
                    if not all(elem in rules.keys() for elem in pointers):
                        found = False
                        break
                    else:
                        built.append(pointers)
                if found:
                    regex = "" if len(built) == 1 else "("
                    for group in built:
                        for pointer in group:
                            regex = regex + rules[pointer]
                        regex = regex + "|"
                    regex = regex[:-1]
                    if len(built) > 1:
                        regex = regex + ")"
                    rules[rule] = regex
    
    total = 0
    input_messages = input_messages.splitlines()
    for input_message in input_messages:
        if re.search("^" + rules["0"] + "$", input_message) != None:
            total = total + 1
    print(total)


if __name__ == "__main__":
    main()
