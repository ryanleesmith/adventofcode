SUM = 22406676
data = []

def main():
    input = open("input.txt", "r")
    data = [int(line) for line in input.read().splitlines()]
    for x in range(len(data)):
        min_val = data[x]
        max_val = 0
        total = data[x]
        for y in range(x + 1, len(data)):
            min_val = min(data[y], min_val)
            max_val = max(data[y], max_val)
            total = total + data[y]
            if total == SUM:
                print(min_val + max_val)

if __name__ == "__main__":
    main()
