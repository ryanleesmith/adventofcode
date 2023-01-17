def main():
    neighbors = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    data = read()
    locByLetter = {}
    locByPoint = {}
    graph = {}
    for y, row in enumerate(data):
        for x, letter in enumerate(row):
            if not letter in locByLetter:
                locByLetter[letter] = []
            locByLetter[letter].append([x, y])
            locByPoint["{}, {}".format(x, y)] = letter
    sPoint = "{}, {}".format(locByLetter["S"][0][0], locByLetter["S"][0][1])
    graph[sPoint] = []
    for neighbor in neighbors:
        x, y = [x + y for x, y in zip(locByLetter["S"][0], neighbor)]
        testPoint = "{}, {}".format(x, y)
        if testPoint in locByPoint and (locByPoint[testPoint] == "a" or locByPoint[testPoint] == "b"):
            graph[sPoint].append(testPoint)
    ePoint = "{}, {}".format(locByLetter["E"][0][0], locByLetter["E"][0][1])
    graph[ePoint] = []
    for neighbor in neighbors:
        x, y = [x + y for x, y in zip(locByLetter["E"][0], neighbor)]
        testPoint = "{}, {}".format(x, y)
        if testPoint in locByPoint and (locByPoint[testPoint] == "y" or locByPoint[testPoint] == "z"):
            graph[ePoint].append(testPoint)
    for i in range(97, 123):
        char = chr(i)
        for idx in range(len(locByLetter[char])):
            point = "{}, {}".format(locByLetter[char][idx][0], locByLetter[char][idx][1])
            graph[point] = []
            for neighbor in neighbors:
                x, y = [x + y for x, y in zip(locByLetter[char][idx], neighbor)]
                testPoint = "{}, {}".format(x, y)
                testChar = "E" if i == 122 else chr(i+1)
                if testPoint in locByPoint and (locByPoint[testPoint] == char or locByPoint[testPoint] == testChar):
                    graph[point].append(testPoint)
                elif testPoint in locByPoint and (i != 97 and i > ord(locByPoint[testPoint])):
                    graph[point].append(testPoint)

    path = len(shortest_path(graph, sPoint, ePoint)) - 1
    for idx in range(len(locByLetter["a"])):
        alt = len(shortest_path(graph, "{}, {}".format(locByLetter["a"][idx][0], locByLetter["a"][idx][1]), ePoint)) - 1
        if alt != -1:
            path = min(path, alt)
    print(path)

def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0

    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]

        if node2 in next_nodes:
            current_path.append(node2)
            return current_path

        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)

                previous_nodes.add(next_node)

        path_index += 1

    return []

def read():
    input = open("input.txt", "r")
    return [[i for i in list(line)] for line in input.read().splitlines()]

if __name__ == "__main__":
    main()
