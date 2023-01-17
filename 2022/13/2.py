def main():
    data = read()
    groups = []
    for group in data:
        for packet in group:
            exec("groups.append({})".format(packet))
    idxs = [0, 0]
    for group in groups:
        if battle([2], group) == -1:
            idxs[0] = idxs[0] + 1
    for group in groups:
        if battle([6], group) == -1:
            idxs[1] = idxs[1] + 1
    print((idxs[0] + 1) * (idxs[1] + 2))

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
