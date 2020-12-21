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
    global accumulator, offset, instructions

    input = open("input.txt", "r")
    instructions = [Instruction(line.split()) for line in input.read().splitlines()]

    for (idx, instruction) in enumerate(instructions):
        if instructions[idx].operation == "jmp":
            instructions[idx].operation = "nop"
        elif instructions[idx].operation == "nop":
            instructions[idx].operation = "jmp"
        try:
            while True and offset != len(instructions):
                instructions[offset].call()
            print(accumulator)
            break
        except Exception:
            accumulator = 0
            offset = 0
            for instruction in instructions:
                instruction.count = 0
        if instructions[idx].operation == "nop":
            instructions[idx].operation = "jmp"
        elif instructions[idx].operation == "jmp":
            instructions[idx].operation = "nop"

if __name__ == "__main__":
    main()
