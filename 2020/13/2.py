from functools import reduce

def main():
    input = open("input.txt", "r")
    data = input.read().splitlines()[1]
    divisors = []
    remainders = []
    for idx, val in enumerate(data.split(",")):
        if val == "x":
            continue
        divisors.append(int(val))
        remainders.append(int(val) - idx)

    print(remainder(divisors, remainders))

def remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

if __name__ == "__main__":
    main()
