def main():
    input = open("input.txt", "r")
    print(sum(map(lambda (idx, line): check(idx, line), enumerate(input.read().splitlines()[1::1]))))

def check(idx, line):
    return line[((idx + 1) * 3) % len(line)] == "#"

if __name__ == "__main__":
    main()
