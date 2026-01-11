import random

class Agent:
    def __init__(self):
        self.energy = random.random()
        self.memory = []

    def act(self, world):
        self.energy += world.signal() * 0.1
        self.memory.append(self.energy)

    def fitness(self):
        return self.energy
      
