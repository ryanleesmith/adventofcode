def main():
    fish = read()
    dupes = {i:fish.count(i) for i in fish}
    coming = {}
    for i in range(80):
        (dupes, coming) = run(dupes, coming)
    print(sum(dupes.values()) + sum(coming.values()))

def run(dupes, coming):
    for (days, fish) in coming.items():
        coming[days - 1] = fish
        del coming[days]

    for (days, fish) in dupes.items():
        dupes[days - 1] = fish
        del dupes[days]

    if dupes.has_key(-1):
        dupes[6] = dupes[-1]
        del dupes[-1]
        coming[2] = dupes[6]

    if coming.has_key(0):
        dupes[6] = (dupes[6] if dupes.has_key(6) else 0) + coming[0]
        del coming[0]

    return (dupes, coming)

def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read().split(",")]

if __name__ == "__main__":
    main()
