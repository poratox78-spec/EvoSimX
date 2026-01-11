import random

class World:
    def __init__(self, bias=0.0):
        self.bias = bias

    def signal(self):
        return random.uniform(-1, 1) + self.bias
        
