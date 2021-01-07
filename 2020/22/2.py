from collections import deque
from copy import deepcopy
from itertools import islice

def main():
    players = []

    input = open("input.txt", "r")
    players = [deque(reversed([int(card) for card in player.splitlines()[1::]])) for player in input.read().split("\n\n")]
    play(players)
    print(sum([card * (idx + 1) for (idx, card) in enumerate(sorted(players, key=len, reverse=True)[0])]))

def play(players):
    rounds = []
    while len(players[0]) > 0 and len(players[1]) > 0:
        round = "".join(str(i) for i in players[0]).join("/").join(str(i) for i in players[1])
        if round in rounds:
            raise Exception
        else:
            rounds.append(round)

        cards = [players[0].pop(), players[1].pop()]
        if len(players[0]) >= cards[0] and len(players[1]) >= cards[1]:
            sub = deepcopy(players)
            for i in range(2):
                sub[i] = deque(islice(sub[i], len(sub[i]) - cards[i], len(sub[i])))
            try:
                play(sub)
                winner = 0 if len(sub[0]) > 0 else 1
            except Exception:
                winner = 0
            cards = cards if winner == 0 else list(reversed(cards))
        else:
            winner = cards.index(max(cards))
            cards = sorted(cards, reverse=True)
        players[winner].extendleft(cards)

    return

if __name__ == "__main__":
    main()
