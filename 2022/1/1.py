def main():
    print(max(list(map(lambda calories: sum(calories), [[int(i) for i in line.splitlines()] for line in open("input.txt", "r").read().split("\n\n")]))))

if __name__ == "__main__":
    main()
