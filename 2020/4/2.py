import re

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def main():
    input = open("input.txt", "r")
    print(sum(map(lambda passport: check(passport), input.read().split("\n\n"))))

def check(passport):
    global fields
    return sum(map(lambda entry: read(entry), passport.split())) == len(fields)

def read(entry):
    global fields
    data = entry.split(":")
    valid = False
    if data[0] == "byr":
        valid = 1920 <= int(data[1]) <= 2002
    elif data[0] == "iyr":
        valid = 2010 <= int(data[1]) <= 2020
    elif data[0] == "eyr":
        valid = 2020 <= int(data[1]) <= 2030
    elif data[0] == "hgt":
        if data[1][-2::1] == "cm":
            valid = 150 <= int(data[1][:-2]) <= 193
        elif data[1][-2::1] == "in":
            valid = 59 <= int(data[1][:-2]) <= 76
    elif data[0] == "hcl":
        valid = re.search("#([0-9]|[a-f]){6}", data[1]) != None
    elif data[0] == "ecl":
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        valid = data[1] in colors
    elif data[0] == "pid":
        try:
            int(data[1])
            valid = re.search("([0-9]){9}", data[1]) != None and len(data[1]) == 9
        except ValueError:
            valid = False

    return valid

if __name__ == "__main__":
    main()
