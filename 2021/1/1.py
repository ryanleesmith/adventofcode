def main():
    data = read()
    last = 0
    count = 0
    for i in range(len(data)):
        if last != 0 and data[i] > last:
            count = count + 1
        last = data[i]
    print(count)

def read():
    data = []
    input = open("input.txt", "r")
    for line in input.read().splitlines():
        data.append(int(line))
    return data

if __name__ == "__main__":
    main()
