import numpy as np

def main():
    dots, folds = read()
    maxX = 0
    maxY = 0
    for dot in dots:
        maxX = max(maxX, dot[0] + 1)
        maxY = max(maxY, dot[1] + 1)
    paper = np.full((maxY, maxX), ".", dtype=np.str)
    for dot in dots:
        paper[dot[1]][dot[0]] = "#"
    for fold in folds:
        dots, paper = foldPaper(paper, dots, fold)
        print(sum([len(filter(lambda col: col == "#", row)) for row in paper]))
        break

def foldPaper(paper, dots, fold):
    newDots = []
    paper = paper[:fold[1],:] if fold[1] != 0 else paper[:,:fold[0]]
    for dot in dots:
        if fold[0] != 0 and dot[0] < fold[0] or fold[1] != 0 and dot[1] < fold[1]:
            newDots.append(dot)
        if fold[1] != 0 and dot[1] > fold[1]:
            newDots.append([dot[0], dot[1] - ((dot[1] - fold[1]) * 2)])
            paper[dot[1] - ((dot[1] - fold[1]) * 2)][dot[0]] = "#"
        elif fold[0] != 0 and dot[0] > fold[0]:
            newDots.append([dot[0] - ((dot[0] - fold[0]) * 2), dot[1]])
            paper[dot[1]][dot[0] - ((dot[0] - fold[0]) * 2)] = "#"
    return newDots, paper

def read():
    input = open("input.txt", "r")
    dots, folds = [lines for (lines) in list(line.splitlines() for line in input.read().split("\n\n"))]
    dots = [[int(i) for i in dot.split(',')] for dot in dots]
    folds = [[i for i in fold.split(' ')][2] for fold in folds]
    folds = [[i for i in fold.split('=')] for fold in folds]
    folds = [[int(fold[1]), 0] if fold[0] == 'x' else [0, int(fold[1])] for fold in folds]
    return dots, folds

if __name__ == "__main__":
    main()
