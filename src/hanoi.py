class Hanoi(object):
    def __init__(self, towers=3, blocks=5):
        self.towers = []
        for tower in range(0, towers):
            self.towers.append([])

        for block in range(0, blocks):
            self.towers[0].append(block)


    def displayTowers(self):
        strs = "{} "*len(self.towers)
        gen = (len(t) for t in self.towers)
        print(strs.format(*(gen)))

    def start(self):
        self.__transfer__(0, len(self.towers)-1)


    def __transfer__(self, start, end):
        self.displayTowers()


