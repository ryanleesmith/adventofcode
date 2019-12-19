grid = {}
pos = None

def main():
    data = read()
    x = 0
    y = 0
    for row in data:
        for col in row:
            grid[(x, y)] = col
            if col == "@":
                pos = (x, y)
            x += 1
        x = 0
        y += 1
    print(grid)
    print(pos)

def read():
    _input = open("input.txt", "r")
    return [[*str(i)] for i in _input.read().splitlines()]

if __name__ == "__main__":
    main()