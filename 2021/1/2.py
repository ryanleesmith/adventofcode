def main():
    data = read()
    x = 0
    y = 0
    z = 0
    last = 0
    count = 0
    for i in range(len(data) - 2):
        x = data[i]
        y = data[i+1]
        z = data[i+2]
        if last != 0 and x + y + z > last:
            count = count + 1
        last = x + y + z
    print(count)

def read():
    data = []
    input = open("input.txt", "r")
    for line in input.read().splitlines():
        data.append(int(line))
    return data

if __name__ == "__main__":
    main()
