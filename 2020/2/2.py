def main():
    input = open("input.txt", "r")
    print(sum(map(lambda line: verify(line), input.read().splitlines())))

def verify(line):
    (scope, letter, password) = map(lambda x: x.rstrip(":"), line.split())
    (lower, upper) = map(lambda x: int(x), scope.split("-"))
    return bool(password[lower-1] == letter) ^ (password[upper-1] == letter)

if __name__ == "__main__":
    main()
