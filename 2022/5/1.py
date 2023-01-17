from collections import deque
import re

def main():
    read()

def read():
    input = open("input.txt", "r")
    groups = [group for group in input.read().split("\n\n")]
    stacks = [line for line in groups[0].splitlines()[:-1]]
    d = deque([deque([]), deque([]), deque([]), deque([]), deque([]), deque([]), deque([]), deque([]), deque([])])
    for stack in stacks:
        for idx, i in enumerate(range(1, 35, 4)):
            if list(stack)[i] != ' ':
                d[idx].appendleft(list(stack)[i])

    moves = [line for line in groups[1].splitlines()]
    for move in moves:
        movement = [int(i) for i in re.findall( r'(\d+)', move)]
        for _ in range(min(movement[0], len(d[movement[1] - 1]))):
            d[movement[2] - 1].append(d[movement[1] - 1].pop())
    
    crates = ''
    for stack in d:
        crates = crates + list(stack)[-1]
    print(crates)

if __name__ == "__main__":
    main()
