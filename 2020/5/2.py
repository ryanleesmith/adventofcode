import math

def main():
    input = open("input.txt", "r")
    seats = map(lambda seat: check(seat), input.read().splitlines())
    seats = sorted(seats)
    for idx, seat in enumerate(seats):
        if seat + 1 != seats[idx + 1]:
            print(seat)
            print(seats[idx + 1])
            break

def check(seat):
    rng = [0, 127]
    row_num = sum(map(lambda (idx, row): getPos(idx, row == "F", rng), enumerate(seat[:7])))
    rng = [0, 7]
    col_num = sum(map(lambda (idx, column): getPos(idx, column == "L", rng), enumerate(seat[-3:])))
    return int((row_num * 8) + col_num)

def getPos(idx, isFront, rng):
    split = math.floor((rng[1] - rng[0]) / 2)
    rng[int(isFront)] = rng[int(not isFront)] + split if isFront else rng[int(not isFront)] - split
    return rng[0] if (rng[0] == rng[1]) else 0

if __name__ == "__main__":
    main()
