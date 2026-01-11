class Agent:
    def __init__(self, genome=None):
        self.genome = genome or random.uniform(0.5, 1.5)
        self.energy = random.random()

    def act(self, world, shared_memory):
        delta = world.signal() * self.genome
        self.energy += delta
        shared_memory.write(delta)
        self.energy += shared_memory.read() * 0.01

    def mutate(self):
        if random.random() < 0.1:
            self.genome *= random.uniform(0.9, 1.1)
