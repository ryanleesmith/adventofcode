from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder
import time
import sys
import copy

data = None
doors = {}

total = 0

def get_steps(graph):
    global doors, total

    ends = []
    matrix = []
    for y in range(0, len(graph)):
        row = []
        for x in range(0, len(graph[y])):
            row.append(0 if (graph[y][x].isupper() or graph[y][x] == "#") else 1)
            if graph[y][x].islower():
                ends.append((x, y))
            if graph[y][x] == "@":
                pos = (x, y)
        matrix.append(row)

    min_steps = 0
    steps = 0
    for end in ends:
        grid = Grid(matrix=copy.deepcopy(matrix))
        start = grid.node(pos[0], pos[1])
        end = grid.node(end[0], end[1])
        finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        
        if len(path) > 0:
            new_graph = copy.deepcopy(graph)
            key = new_graph[end.y][end.x]
            new_graph[end.y][end.x] = "@"
            new_graph[start.y][start.x] = "."
            if key.upper() in doors:
                door = doors[key.upper()]
                new_graph[door[1]][door[0]] = "."

            steps += len(path) - 1
            steps += get_steps(new_graph)
            if steps < min_steps or min_steps == 0:
                min_steps = steps
            steps = 0

    return min_steps

def main():
    global data, doors, total

    data = read()
    graph = []
    for y in range(1, len(data) - 1):
        row = []
        for x in range(1, len(data[y]) - 1):
            row.append(data[y][x])
            if data[y][x].isupper():
                doors[data[y][x]] = (x - 1, y - 1)
        graph.append(row)

    print(get_steps(graph))

def read():
    _input = open("input.txt", "r")
    return [[*str(i)] for i in _input.read().splitlines()]

if __name__ == "__main__":
    main()