fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def main():
    input = open("input.txt", "r")
    print(sum(map(lambda passport: check(passport), input.read().split("\n\n"))))

def check(passport):
    global fields
    return sum(map(lambda entry: read(entry), passport.split())) == len(fields)

def read(entry):
    global fields
    return entry.split(":")[0] in fields

if __name__ == "__main__":
    main()
