class Cups:
    def __init__(self):
        self.head = None
        self.curr = None
        self.tail = None
        self.key = {}

    def insert(self, label):
        cup = Cup(label)
        self.key[label] = cup
        
        if self.tail:
            self.tail.setNext(cup)

        if not self.head:
            self.head = cup
            self.curr = self.head

        cup.setNext(self.head)
        self.tail = cup

    def get(self, label):
        try:
            return self.key[label]
        except KeyError:
            return None

    def getMax(self, playing):
        return self.key[max({k for k in self.key.keys() if k not in playing})]

    def getNext(self):
        next = self.curr.getNext()
        jump = next
        for _ in range(3):
            jump = jump.getNext()
        self.curr.setNext(jump)

    def getPlaying(self):
        cup = self.curr
        playing = []
        for _ in range(3):
            cup = cup.getNext()
            playing.append(cup.getLabel())
        return playing

    def __str__(self):
        cup = self.key[1].getNext()
        output = ""
        while cup:
            output = output + str(cup.getLabel())
            cup = cup.getNext()
            cup = None if cup == self.key[1] else cup
        return output

class Cup:
    def __init__(self, label, next=None):
        self.label = label
        self.next = next

    def getLabel(self):
        return self.label

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

def main():
    cups = Cups()
    [cups.insert(int(x)) for x in str(167248359)]

    for _ in range(100):
        dest = cups.curr.getLabel() - 1
        playing = cups.getPlaying()
        while dest in playing:
            dest = dest - 1
        dest = cups.get(dest)
        if not dest:
            dest = cups.getMax(playing)
        lastPlaying = cups.get(playing[2])
        cups.curr.setNext(lastPlaying.getNext())
        lastPlaying.setNext(dest.getNext())
        dest.setNext(cups.get(playing[0]))
        cups.curr = cups.curr.getNext()

    print(cups)
    return

if __name__ == "__main__":
    main()
