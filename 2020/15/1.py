def main():
    starting = [9,19,1,6,0,5,4]
    spoken = {}

    for turn in range(1, 2021):
        if turn <= len(starting):
            prev = starting[turn-1]
            spoken[prev] = (turn, 0)
        else:
            if prev in spoken:
                if spoken[prev][1] == 0:
                    prev = 0
                else:
                    prev = spoken[prev][1] - spoken[prev][0]

            if prev in spoken:
                if spoken[prev][1] == 0:
                    spoken[prev] = (spoken[prev][0], turn)
                else:
                    spoken[prev] = (spoken[prev][1], turn)
            else:
                spoken[prev] = (turn, 0)

    print(prev)

if __name__ == "__main__":
    main()
