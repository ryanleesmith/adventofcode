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
    total = 0
    operation = ""
    numeral = ""
    for char in exp:
        if char.isdigit():
            numeral = numeral + char
        else:
            if total == 0:
                total = int(numeral)
            else:
                if operation == "+":
                    total = total + int(numeral)
                elif operation == "*":
                    total = total * int(numeral)
            operation = char
            numeral = ""
    if operation == "+":
        total = total + int(numeral)
    elif operation == "*":
        total = total * int(numeral)
    return total

if __name__ == "__main__":
    main()
