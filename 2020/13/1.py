def main():
    input = open("input.txt", "r")
    lines = [line for line in input.read().splitlines()]
    timestamp = int(lines[0])
    ids = [int(id) for id in list(filter(lambda x: x != "x", lines[1].split(",")))]

    for i in range(timestamp, timestamp + 1000):
        for id in ids:
            if i % id == 0:
                print((i - timestamp) * id)
                return


if __name__ == "__main__":
    main()
