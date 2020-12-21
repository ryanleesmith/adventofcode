accumulator = 0
offset = 0
instructions = []

class Instruction:
    def __init__(self, data):
        self.operation = data[0]
        self.argument = int(data[1])
        self.count = 0

    def call(self):
        global accumulator, offset

        self.count = self.count + 1
        if self.count > 1:
            raise Exception
        if self.operation == "acc":
            accumulator = accumulator + self.argument
            offset = offset + 1
        elif self.operation == "jmp":
            offset = offset + self.argument
        elif self.operation == "nop":
            offset = offset + 1

def main():
    input = open("input.txt", "r")
    instructions = [Instruction(line.split()) for line in input.read().splitlines()]
    try:
        while True:
            instructions[offset].call()
    except Exception:
        print(accumulator)

if __name__ == "__main__":
    main()
