from collections import deque

def main():
    players = []

    input = open("input.txt", "r")
    players = [deque(reversed([int(card) for card in player.splitlines()[1::]])) for player in input.read().split("\n\n")]
    while len(players[0]) > 0 and len(players[1]) > 0:
        cards = [players[0].pop(), players[1].pop()]
        players[cards.index(max(cards))].extendleft(sorted(cards, reverse=True))
    
    print(sum([card * (idx + 1) for (idx, card) in enumerate(sorted(players, key=len, reverse=True)[0])]))

if __name__ == "__main__":
    main()
