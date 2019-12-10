layers = []

def main():
    data = read()

    pixel = 0
    min_layer = None
    for _ in range(int(len(data) / (25 * 6))):
        layer = []

        for h in range(0, 6):
            for w in range(0, 25):
                layer.append(data[pixel])
                pixel += 1

        if min_layer is None or layer.count(0) < min_layer.count(0):
            min_layer = layer

    print(min_layer.count(1) * min_layer.count(2))


def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read()]

if __name__ == "__main__":
    main()