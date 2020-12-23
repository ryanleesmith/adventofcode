adapters = []

def main():
    input = open("input.txt", "r")
    adapters = sorted([int(line) for line in input.read().splitlines()])
    adapters.append(max(adapters) + 3)

    jolts = 0
    diffs = {}
    for (idx, adapter) in enumerate(adapters):
        diff = adapter - jolts
        if diff > 3:
            continue
        if diff not in diffs:
            diffs[diff] = 1
        else:
            diffs[diff] = diffs[diff] + 1
        jolts = adapter

    print(diffs[1] * diffs[3])

if __name__ == "__main__":
    main()
