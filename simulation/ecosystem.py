from core.population import Population
from simulation.world import World
import random

class Ecosystem:
    def __init__(self):
        # Création des mondes avec bias initial
        self.worlds = {
            "A": World(bias=0.2),
            "B": World(bias=0.0),
            "C": World(bias=-0.2)
        }
        # Création des populations
        self.populations = {
            k: Population(size=50) for k in self.worlds
        }

    def step(self):
        """
        Un pas de simulation :
        1️⃣ Chaque population agit dans son monde
        2️⃣ Le monde s'adapte à la population
        3️⃣ Migration rare entre populations
        """
        for k in self.populations:
            # 1️⃣ Chaque population agit
            self.populations[k].step(self.worlds[k])

            # 2️⃣ Mise à jour du monde (environnement adaptatif)
            self.worlds[k].update(self.populations[k])

        # 3️⃣ Migration aléatoire
        self.migrate()

    def migrate(self):
        """
        Petite migration aléatoire pour éviter la consanguinité
        """
        if random.random() < 0.05:  # 5 % de chance de migration à chaque pas
            a, b = random.sample(list(self.populations.keys()), 2)
            migrant = random.choice(self.populations[a].agents)
            self.populations[b].agents.append(migrant)
