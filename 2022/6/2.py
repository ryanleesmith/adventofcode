def main():
    markers = read()
    for i in range(0, len(markers)):
        if len(list(dict.fromkeys(markers[i:i+14]))) == 14:
            print(i + 14)
            break

def read():
    return list(open("input.txt", "r").read())

if __name__ == "__main__":
    main()
