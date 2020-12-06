import math

def main():
    input = open("input.txt", "r")
    print(sum(map(lambda group: checkGroup(group), input.read().split("\n\n"))))

def checkGroup(group):
    groupAnswers = {}
    map(lambda answers: checkAnswers(answers, groupAnswers), group.split("\n"))
    return len(groupAnswers)

def checkAnswers(answers, groupAnswers):
    map(lambda answer: setAnswer(answer, groupAnswers), answers)

def setAnswer(answer, groupAnswers):
    groupAnswers[answer] = True

if __name__ == "__main__":
    main()
