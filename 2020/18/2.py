def main():
    input = open("input.txt", "r")
    total = 0
    for line in input.read().splitlines():
        chars = list(line.replace(" ", ""))
        opening = -1
        found = True
        while found:
            found = False
            for (idx, char) in enumerate(chars):
                if char == "(":
                    found = True
                    opening = idx + 1
                if char == ")":
                    chars[opening-1:idx+1] = str(parse(chars[opening:idx]))
                    break
        total = total + parse(chars)
    print(total)

def parse(exp):
    add_done = False
    while not add_done:
        add_done = True
        total = 0
        operation = ""
        numeral = ""
        starting = -1
        for (idx, char) in enumerate(exp):
            if char.isdigit():
                if starting == -1:
                    starting = idx
                numeral = numeral + char
            else:
                if char == "*":
                    if total != 0 and numeral != "":
                        idx = idx - 1
                        break
                    starting = -1
                    numeral = ""
                    continue
                else:
                    add_done = False
                if total == 0:
                    total = int(numeral)
                    numeral = ""
                operation = char
    
                if numeral != "":
                    total = total + int(numeral)
                    exp[starting:idx] = str(total)
                    operation = ""
                    numeral = ""
                    break

        if operation == "+" and numeral != "":
            total = total + int(numeral)
            exp[starting:idx+1] = str(total)

    mul_done = False
    while not mul_done:
        mul_done = True
        total = 0
        operation = ""
        numeral = ""
        starting = -1
        for (idx, char) in enumerate(exp):
            if char.isdigit():
                if starting == -1:
                    starting = idx
                numeral = numeral + char
            else:
                operation = char
                mul_done = False
                if total == 0:
                    total = int(numeral)
                    numeral = ""
    
                if operation == "*" and numeral != "":
                    total = total * int(numeral)
                    exp[starting:idx] = str(total)
                    operation = ""
                    numeral = ""
                    break

        if operation == "*" and numeral != "":
            total = total * int(numeral)
            exp[starting:idx+1] = str(total)
    
    return int(''.join(exp))

if __name__ == "__main__":
    main()
