def main():
    data = read()
    horizontal = 0
    vertical = 0
    aim = 0
    for i in range(len(data)):
        if data[i][0] == "forward":
            horizontal = horizontal + data[i][1]
            vertical = vertical + (data[i][1] * aim)
        if data[i][0] == "down":
            aim = aim + data[i][1]
        if data[i][0] == "up":
            aim = aim - data[i][1]
    print(horizontal * vertical)

def read():
    data = []
    input = open("input.txt", "r")
    for line in input.read().splitlines():
        direction = line.split(" ")
        data.append([direction[0], int(direction[1])])
    return data

if __name__ == "__main__":
    main()
