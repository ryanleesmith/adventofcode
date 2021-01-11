class Tile:
    def __init__(self, num):
        self.color = 0 # White
        self.num = num
        self.neighbors = {'e': None, 'se': None, 'sw': None, 'w': None, 'nw': None, 'ne': None}

    def getNeighbor(self, neighbor):
        return self.neighbors[neighbor]

    def setNeighbor(self, neighbor, tile):
        self.neighbors[neighbor] = tile

def main():
    tiles = []
    ordered = ['e', 'ne', 'nw', 'w', 'sw', 'se']
    neighbors = ['w', 'nw', 'ne', 'e', 'se', 'sw', 'w']
    relation = {'e': 'w', 'w': 'e', 'se': 'nw', 'nw': 'se', 'sw': 'ne', 'ne': 'sw'}
    reference = None
    prev = None
    for ring in range(1, 50):
        if ring == 1:
            reference = Tile(1)
            tiles.append(reference)
            prev = reference
        else:
            counter = 2
            for i in range(ring - 1):
                counter = counter + (6 * i)
            for (idx, neighbor) in enumerate(neighbors):
                if idx == 0:
                    tile = Tile(counter)
                    tiles.append(tile)
                    counter = counter + 1
                    tile.setNeighbor(neighbor, prev)
                    prev.setNeighbor(relation[neighbor], tile)
                    relative_idx = ordered.index(neighbor) + 1
                    relative = prev.getNeighbor(ordered[(relative_idx + 1) % 6])
                    if relative:
                        tile.setNeighbor(ordered[relative_idx % 6], relative)
                        relative.setNeighbor(relation[ordered[relative_idx % 6]], tile)
                    
                    prev = tile
                else:
                    count = ring - 2 if idx == 1 else ring - 1
                    for _ in range(count):
                        tile = Tile(counter)
                        tiles.append(tile)
                        counter = counter + 1
                        tile.setNeighbor(neighbor, prev)
                        prev.setNeighbor(relation[neighbor], tile)
                        relative_idx = ordered.index(neighbor) + 1
                        relative = prev
                        for i in range(2):
                            relative = relative.getNeighbor(ordered[(relative_idx + i + 1) % 6])
                            if relative:
                                tile.setNeighbor(ordered[(relative_idx + i) % 6], relative)
                                relative.setNeighbor(relation[ordered[(relative_idx + i) % 6]], tile)
                        prev = tile

    input = open("input.txt", "r")
    for line in input.read().splitlines():
        tile = reference
        neighbor = ""
        for char in list(line):
            neighbor = neighbor + char
            if neighbor in ordered:
                tile = tile.getNeighbor(neighbor)
                neighbor = ""
        tile.color ^= 1

    print(len(filter(lambda tile: tile.color, tiles)))
if __name__ == "__main__":
    main()
