import numpy as np

width = 25
height = 6

def main():
    global width, height

    data = read()

    pixel = 0
    layers = []
    for _ in range(int(len(data) / (width * height))):
        rows = []
        for h in range(0, height):
            row = []
            for w in range(0, width):
                row.append(data[pixel])
                pixel += 1
            rows.append(row)
        layers.append(np.array(rows))
    
    image = []
    for h in range(0, height):
        row = []
        for w in range(0, width):
            transparent = True
            while transparent:
                for layer in layers:
                    if layer[h].flat[w] != 2:
                        row.append(str(layer[h].flat[w]).replace("0", " ").replace("1", "#"))
                        transparent = False
                        break
        image.append(row)
    for row in np.array(image):
        print(*row, sep="")

def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read()]

if __name__ == "__main__":
    main()