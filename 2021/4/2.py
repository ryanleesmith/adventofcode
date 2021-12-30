def main():
    data = read()
    for i in range(5, len(data[0]) + 1):
        for (idx, board) in enumerate(data[1]):
            winner = isWinner(data[0][:i], board)
            if winner != None:
                del data[1][idx]
            if len(data[1]) == 0:
                print(winner)
                break
        else:
            continue
        break

def isWinner(numbers, board):
    for y in range(0, 5):
        row = []
        for x in range(0, 5):
            row.append(board[x + (5 * y)])
        if all(elem in numbers for elem in row):
            return numbers[-1] * sum(list(set(board).difference(numbers)))

    for x in range(0, 5):
        col = []
        for y in range(0, 5):
            col.append(board[x + (5 * y)])
        if all(elem in numbers for elem in col):
            return numbers[-1] * sum(list(set(board).difference(numbers)))

    return None

def read():
    numbers = []
    boards = []
    board = []
    input = open("input.txt", "r")
    for (idx, line) in enumerate(input.read().splitlines()):
        if idx == 0:
            numbers = [int(i) for i in line.split(",")]
        elif line:
            board.extend([int(i) for i in line.split()])
        else:
            if board:
                boards.append(board)
            board = []
    if board:
        boards.append(board)
    return [numbers, boards]

if __name__ == "__main__":
    main()
