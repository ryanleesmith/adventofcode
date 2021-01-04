def main():
    tiles = []
    input = open("input.txt", "r")
    groups = input.read().split("\n\n")

    for group in groups:
        (name, tile) = group.split(":\n")
        name = int(name[-4:])
        lines = tile.splitlines()
        edges = [lines[0], lines[len(lines) - 1]]
        for x in [0, len(lines[0]) - 1]:
            edge = ""
            for y in range(len(lines)):
                edge = edge + lines[y][x]
            edges.append(edge)
        edges.extend([edges[0][::-1], edges[1][::-1], edges[2][::-1], edges[3][::-1]])
        tiles.append((name, edges))

    total = 1
    for tile in tiles:
        matches = 0
        for edge in tile[1]:
            for other in tiles:
                if tile[0] == other[0]:
                    continue
                for other_edge in other[1]:
                    if edge == other_edge:
                        matches = matches + 1
        if matches == 4:
            total = total * tile[0]

    print(total)

if __name__ == "__main__":
    main()
