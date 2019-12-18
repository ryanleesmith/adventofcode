def main():
    data = read()

    final = []
    for _ in range(10000):
        final += data

    offset = int("".join(str(i) for i in data[:7]))

    for _ in range(100):
        out = []
        total = 0
        for i in range(len(final) - 1, offset - 1, -1):
            total += final[i]
            out.append(total % 10)
        out.reverse()
        final = [0] * offset
        final += out
    print("".join(str(i) for i in out[:8]))

def read():
    _input = open("input.txt", "r")
    return [int(i) for i in _input.read()]

if __name__ == "__main__":
    main()