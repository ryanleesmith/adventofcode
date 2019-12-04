from collections import Counter

def main():
    count = 0
    for i in range(165432, 707912 + 1):
        last_num = 0
        dupes = {}
        for j in range(0, 6):
            num = int(str(i)[j])
            if num < last_num:
                break
            if num == last_num:
                try:
                    dupes[num] += 1
                except KeyError:
                    dupes[num] = 2
            last_num = num
        else:
            if len(dupes) > 0 and min(dupes.values()) == 2 and j == 5:
                count += 1
            continue
    print(count)

if __name__ == "__main__":
    main()