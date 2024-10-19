import random

class Connection:
    def __init__(self, src, dst, weigth):
        self.src = src
        self.dst = dst
        self.weigth = weigth
    
    def mutate_weight(self):
        if random.uniform(0, 1) < 0.1:
            self.weigth = random.uniform(-1, 1)
        else:
            self.weigth += random.gauss(0, 1) / 10
            if self.weigth > 1:
                self.weigth = 1
            if self.weigth < -1:
                self.weigth = -1
    
    def clone(self, src, dst):
        clone = Connection(src, dst, self.weigth)
        return clone
            