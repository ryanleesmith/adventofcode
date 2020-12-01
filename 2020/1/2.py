import math

def main():
    SUM = 2020
    data = read()
    data.sort(reverse=True)
    remove_idx = 0
    for i in range(len(data)):
        if (SUM - data[i] - data[len(data)-2]) < data[len(data)-1]:
            remove_idx = i
    data = data[remove_idx+1:]
    for i in range(len(data)):
        for j in range(len(data) - 2, i + 1, -1):
            for k in range(len(data) - 1, i + 1, -1):
                if (data[i] + data[j] + data[k]) == SUM:
                    print(data[i] * data[j] * data[k])
                    return

def read():
    data = []
    input = open("input.txt", "r")
    for line in input.read().splitlines():
        data.append(int(line))
    return data

if __name__ == "__main__":
    main()
