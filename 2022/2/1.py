def main():
    games = read()
    points = 0
    for game in games:
        points = points + match(game)
    print(points)

def match(game):
    points = 0
    if game[1] == 'X':
        points = points + 1
    elif game[1] == 'Y':
        points = points + 2
    elif game[1] == 'Z':
        points = points + 3
    if game[0] == 'A' and game[1] == 'Y':
        points = points + 6
    elif game[0] == 'B' and game[1] == 'Z':
        points = points + 6
    elif game[0] == 'C' and game[1] == 'X':
        points = points + 6
    elif (game[0] == 'A' and game[1] == 'X') or (game[0] == 'B' and game[1] == 'Y') or (game[0] == 'C' and game[1] == 'Z'):
        points = points + 3
    else:
        points = points + 0
    return points

def read():
    input = open("input.txt", "r")
    return [[i for i in line.split(" ")] for line in input.read().splitlines()]

if __name__ == "__main__":
    main()
