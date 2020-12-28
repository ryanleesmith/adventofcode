import re

def set_bit(position, bit, binary):
    mask = 1 << position
    binary &= ~mask
    if bit:
        binary |= mask
    return binary

def main():
    vals = {}
    input = open("input.txt", "r")
    for line in input.read().splitlines():
        if line[:4] == "mask":
            mask = []
            for idx, val in enumerate(list(line[7:])):
                if val == "X":
                    continue
                mask.append((35 - idx, int(val)))
        else:
            data = re.findall("mem\[(\d+)\] = (\d+)", line)[0]
            addr, val = [int(x) for x in data]
            for bit in mask:
                val = set_bit(bit[0], bit[1], val)
            vals[addr] = val
    print(sum(vals.values()))


if __name__ == "__main__":
    main()
