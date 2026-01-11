from core.agent import Agent
from core.memory import SharedMemory
import random

class Population:
    def __init__(self, size):
        self.size = size
        self.memory = SharedMemory()
        self.agents = [Agent() for _ in range(size)]

    def step(self, world):
        for a in self.agents:
            a.act(world, self.memory)
        self.selection()

    def selection(self):
        # 1️⃣ Trier par fitness (meilleurs en premier)
        self.agents.sort(key=lambda a: a.fitness(), reverse=True)

        # 2️⃣ Garder la moitié la plus performante
        survivors = self.agents[:self.size // 2]

        # 3️⃣ Reproduction avec héritage + mutation
        new_agents = survivors.copy()
        while len(new_agents) < self.size:
            parent = random.choice(survivors)
            child = Agent(genome=parent.genome)
            child.mutate()
            new_agents.append(child)

        # 4️⃣ Remplacer la population
        self.agents = new_agents

    def average_fitness(self):
        return sum(a.fitness() for a in self.agents) / len(self.agents)
