def main():
    markers = read()
    for i in range(0, len(markers)):
        if len(list(dict.fromkeys(markers[i:i+4]))) == 4:
            print(i + 4)
            break

def read():
    return list(open("input.txt", "r").read())

if __name__ == "__main__":
    main()
