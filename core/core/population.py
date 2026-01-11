from core.agent import Agent
import random

class Population:
    def __init__(self, size):
        self.agents = [Agent() for _ in range(size)]

    def step(self, world):
        for a in self.agents:
            a.act(world)
        self.selection()

    def selection(self):
        self.agents.sort(key=lambda a: a.fitness(), reverse=True)
        self.agents = self.agents[:len(self.agents)//2]
        while len(self.agents) < 50:
            self.agents.append(Agent())

    def average_fitness(self):
        return sum(a.fitness() for a in self.agents) / len(self.agents)
      
