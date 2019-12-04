def main():
    count = 0
    for i in range(165432, 707912 + 1):
        last_num = 0
        has_dupe = False
        for j in range(0, 6):
            num = int(str(i)[j])
            if num < last_num:
                break
            if num == last_num:
                has_dupe = True
            last_num = num
        else:
            if has_dupe and j == 5:
                count += 1
            continue
    print(count)

if __name__ == "__main__":
    main()