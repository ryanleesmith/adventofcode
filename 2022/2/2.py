def main():
    games = read()
    points = 0
    for game in games:
        points = points + match(game)
    print(points)

def match(game):
    points = 0
    player = ''
    if game[1] == 'X':
        if game[0] == 'A':
            player = 'Z'
        elif game[0] == 'B':
            player = 'X'
        elif game[0] == 'C':
            player = 'Y'
    elif game[1] == 'Y':
        if game[0] == 'A':
            player = 'X'
        elif game[0] == 'B':
            player = 'Y'
        elif game[0] == 'C':
            player = 'Z'
    if game[1] == 'Z':
        if game[0] == 'A':
            player = 'Y'
        elif game[0] == 'B':
            player = 'Z'
        elif game[0] == 'C':
            player = 'X'

    if player == 'X':
        points = points + 1
    elif player == 'Y':
        points = points + 2
    elif player == 'Z':
        points = points + 3
    if game[0] == 'A' and player == 'Y':
        points = points + 6
    elif game[0] == 'B' and player == 'Z':
        points = points + 6
    elif game[0] == 'C' and player == 'X':
        points = points + 6
    elif (game[0] == 'A' and player == 'X') or (game[0] == 'B' and player == 'Y') or (game[0] == 'C' and player == 'Z'):
        points = points + 3
    else:
        points = points + 0
    return points

def read():
    input = open("input.txt", "r")
    return [[i for i in line.split(" ")] for line in input.read().splitlines()]

if __name__ == "__main__":
    main()
