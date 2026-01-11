from core.population import Population
from simulation.world import World
import random

class Ecosystem:
    def __init__(self):
        self.worlds = {
            "A": World(bias=0.2),
            "B": World(bias=0.0),
            "C": World(bias=-0.2)
        }
        self.populations = {
            k: Population(size=50) for k in self.worlds
        }

    def step(self):
        for k in self.populations:
            self.populations[k].step(self.worlds[k])

        self.migrate()

    def migrate(self):
        if random.random() < 0.05:
            a, b = random.sample(list(self.populations.keys()), 2)
            migrant = random.choice(self.populations[a].agents)
            self.populations[b].agents.append(migrant)
  
