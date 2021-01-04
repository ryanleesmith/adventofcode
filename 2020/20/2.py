import math

def main():
    pieces = {}
    solved = []
    tiles = {}
    corners = {}
    input = open("input.txt", "r")
    groups = input.read().split("\n\n")

    for group in groups:
        (name, tile) = group.split(":\n")
        name = int(name[-4:])
        lines = tile.splitlines()

        tile_pos = []
        for line in lines:
            row = []
            for char in list(line):
                row.append(char)
            tile_pos.append(row)
        pieces[name] = tile_pos

        edges = [lines[0], "", lines[len(lines) - 1][::-1], ""]
        for x in [len(lines[0]) - 1, 0]:
            edge = ""
            for y in range(len(lines)):
                edge = edge + lines[y][x]
            if x == 0:
                edges[3] = edge[::-1]
            else:
                edges[1] = edge
        edges.extend([edges[2][::-1], edges[1][::-1], edges[0][::-1], edges[3][::-1]])
        tiles[name] = edges

    for (name, edges) in tiles.items():
        matches = 0
        matched = []
        for edge in edges:
            for (other_name, other_edges) in tiles.items():
                if name == other_name:
                    continue
                for other_edge in other_edges:
                    if edge == other_edge[::-1]:
                        matches = matches + 1
                        matched.append(edges.index(edge))
        if matches == 4:
            corner = (matched[0], matched[1])
            if not corner in corners:
                corners[corner] = [name]
            else:
                corners[corner].append(name)
            corner = (matched[2], matched[3])
            if not corner in corners:
                corners[corner] = [name]
            else:
                corners[corner].append(name)

    if (1, 2) in corners:
        solved = [[(corners[(1, 2)][0], 0, 0)]]
    elif (2, 3) in corners:
        solved = [[(corners[(2, 3)][0], 0, 1)]]
        rotated = []
        for rtx in range(1, 5):
            rotated.append(tiles[corners[(2, 3)][0]][(rtx % 4) % 4])
        tiles[corners[(2, 3)][0]] = rotated

    x = 1
    y = 0
    size = int(math.sqrt(len(tiles)))
    while y < size:
        for i in range(x, size):
            if i == 0:
                solved.append([])
                testing = solved[y-1][i]
            else:
                testing = solved[y][i-1]

            for (name, edges) in tiles.items():
                if name == testing[0]:
                    continue
                for (idx, edge) in enumerate(edges):
                    if i == 0:
                        if edge[::-1] == tiles[testing[0]][2]:
                            rotated = []
                            offset = 0 if idx < 4 else 4
                            for rtx in range(4):
                                rotated.append(edges[(rtx + idx % 4) % 4 + offset])
                            tiles[name] = rotated
                            rotate_amt = abs((idx % 4) - 4)
                            solved[y].append((name, 0 if idx < 4 else 1, rotate_amt))
                            break
                    else:
                        if edge[::-1] == tiles[testing[0]][1]:
                            rotated = []
                            offset = 0 if idx < 4 else 4
                            for rtx in range(4):
                                rotated.append(edges[(rtx + (idx + 1) % 4) % 4 + offset])
                            tiles[name] = rotated
                            rotate_amt = abs(((idx + 1) % 4) - 4)
                            solved[y].append((name, 0 if idx < 4 else 1, rotate_amt))
                            break
        x = 0
        y = y + 1

    for (y, row) in enumerate(solved):
        for (x, col) in enumerate(row):
            solved_tile = pieces[col[0]]
            if col[1]:
                solved_tile = flip(solved_tile)
            for _ in range(col[2]):
                solved_tile = rotate(solved_tile)
            solved[y][x] = solved_tile

    final = []
    for y in range(size):
        for line in range(1, 9):
            row = []
            for x in range(size):
                row.extend(solved[y][x][line][1:-1])
            final.append(row)

    monster = [(0,0),(1,1),(4,1),(5,0),(6,0),(7,1),(10,1),(11,0),(12,0),(13,1),(16,1),(17,0),(18,-1),(18,0),(19,0)]
    size = len(final)

    count = 0
    works = False
    monsters = 0
    while not works:
        for y in range(1, size - 1):
            for x in range(0, size - 19):
                found = True
                for idx in range(len(monster)):
                    if final[monster[idx][1] + y][monster[idx][0] + x] != "#":
                        found = False
                if found:
                    works = True
                    monsters = monsters + 1
                    for idx in range(len(monster)):
                        convert = list(final[monster[idx][1] + y])
                        convert[monster[idx][0] + x] = "O"
                        final[monster[idx][1] + y] = convert
        if monsters == 0:
            final = rotate(final)
            count = count + 1
            if count == 4:
                final = flip(final)
    
    output(final)
    print([x for l in final for x in l].count("#"))

def flip(tile):
    return list(reversed(tile))

def rotate(tile):
    return list(zip(*reversed(tile)))

def output(tile):
    size = len(tile)
    for y in range(size):
        line = ""
        for x in range(size):
            line = line + tile[y][x]
        print(line)

if __name__ == "__main__":
    main()
