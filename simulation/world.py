import random

class World:
    def __init__(self, bias=0.0):
        self.bias = bias

    def signal(self):
        return random.uniform(-1, 1) + self.bias
        
class World:
    def __init__(self, bias=0.0):
        self.bias = bias
        self.pressure = 0.0

    def signal(self):
        return random.uniform(-1, 1) + self.bias - self.pressure

    def update(self, population):
        self.pressure = population.average_fitness() * 0.01
        
