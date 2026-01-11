import random

class Agent:
    def __init__(self, genome=None):
        # Génome : influence de l'agent sur les signaux
        self.genome = genome or random.uniform(0.5, 1.5)
        # Énergie initiale
        self.energy = random.random()
        # Mémoire locale (liste d'historique simplifiée)
        self.memory = []

    def act(self, world, shared_memory):
        """
        Action de l'agent :
        - reçoit le signal du monde
        - ajoute l'effet de la mémoire partagée
        - stocke les delta dans la mémoire collective
        """
        delta = world.signal() * self.genome
        self.energy += delta
        # écrire dans mémoire collective
        shared_memory.write(delta)
        # influence de la mémoire collective
        self.energy += shared_memory.read() * 0.01
        # sauvegarde locale
        self.memory.append(self.energy)

    def mutate(self):
        """
        Mutation du génome avec faible variation aléatoire
        """
        if random.random() < 0.1:  # 10 % de chance de mutation
            self.genome *= random.uniform(0.9, 1.1)

    def fitness(self):
        """
        Fonction de fitness : ici énergie actuelle
        """
        return self.energy
