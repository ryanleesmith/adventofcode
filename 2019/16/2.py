def main():
    pattern = [0, 1, 0, -1]

    data = read()
    offset = int("".join(str(i) for i in data[:7]))
    offset = ((len(data) * 10000) - offset) % len(data) - 1
    print(offset)

    for _ in range(100):
        out = []
        round = 1
        for _ in data:
            match = 0
            compare = round - 1
            pos = 0
            idx = 1
            val = 0
            for i in data:
                mult = i * pattern[pos % 4]
                try:
                    if idx % compare == match:
                        pos += 1
                        compare = round
                        match = compare - 1
                except ZeroDivisionError:
                    pos += 1
                    mult = i * pattern[pos % 4]

                val += mult
                idx += 1
            parts = [*str(abs(val))]
            out.append(int(parts[len(parts) - 1]))
            round += 1
        data = out
        print("".join(str(i) for i in data[offset:offset + 8]))

def read():
    _input = open("input.txt", "r")
    return [int(i) for i in _input.read()]

if __name__ == "__main__":
    main()