import game_of_life.cell as cell

class Grid:
    def __init__(self, fmap):
        self.fmap = fmap
    
    def initialize(self):
        self.map = list()
        self.n = 0
        with open(self.fmap) as mp:
            for line in mp.readlines():
                self.n += 1
                line = line.strip()
                li = list()
                for cell in line:
                    li.append(cell)
                self.map.append(li)
            self.m = len(line)
        mp.close()

    def update(self):
        self.new_map = [row[:] for row in self.map]
        for i in range(self.n):
            for j in range(self.m):
                cell.cellUpdate(self.map, self.new_map, i, j, self.n, self.m)
        self.map = self.new_map
            

    def show(self):
        for line in self.map:
            for cell in line:
                print(cell, end='')
            print()