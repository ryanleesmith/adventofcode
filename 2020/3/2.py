import numpy

def main():
    input = open("input.txt", "r")
    data = input.read()
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(numpy.prod(map(lambda slope: calc(data.splitlines()[slope[1]::slope[1]], slope[0]), slopes)))

def calc(data, right):
    return sum(map(lambda (idx, line): check(idx, line, right), enumerate(data)))

def check(idx, line, right):
    return line[((idx + 1) * right) % len(line)] == "#"

if __name__ == "__main__":
    main()
