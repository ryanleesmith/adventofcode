import re
from itertools import  product

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
            float_targets = []
            float_vals = []
            for idx, val in enumerate(list(line[7:])):
                if val == "X":
                    float_targets.append(35 - idx)
                else:
                    mask.append((35 - idx, int(val)))
            float_vals = [p for p in product([0, 1], repeat=len(float_targets))]
        else:
            data = re.findall("mem\[(\d+)\] = (\d+)", line)[0]
            addr, val = [int(x) for x in data]
            for bit in mask:
                if bit[1] == 1:
                    addr = set_bit(bit[0], bit[1], addr)

            for float_set in float_vals:
                float_mask = []
                for idx, float_target in enumerate(float_targets):
                    float_mask.append((float_target, float_set[idx]))

                for bit in float_mask:
                    addr = set_bit(bit[0], bit[1], addr)

                vals[addr] = val
    print(sum(vals.values()))


if __name__ == "__main__":
    main()
