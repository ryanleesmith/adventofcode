def main():
    data = read()
    groups = []
    for group in data:
        pair = []
        for packet in group:
            exec("pair.append({})".format(packet))
        groups.append(pair)
    res = 0
    for idx, group in enumerate(groups):
        if battle(group[0], group[1]) == 1:
            res = res + idx + 1
    print(res)

def battle(left, right):
    if type(left) is not list and type(right) is not list:
        if int(left) < int(right):
            return 1
        elif int(left) > int(right):
            return -1
        else:
            return 0
    left = left if type(left) is list else [left]
    right = right if type(right) is list else [right]
    for idx in range(len(left)):
        if idx > len(right) - 1:
            return -1
        ret = battle(left[idx], right[idx])
        if ret != 0:
            return ret
    return 1 if len(right) > len(left) else 0

def read():
    input = open("input.txt", "r")
    return [[i for i in line.splitlines()] for line in input.read().split("\n\n")]

if __name__ == "__main__":
    main()
