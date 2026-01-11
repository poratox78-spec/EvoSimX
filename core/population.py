from core.memory import SharedMemory

class Population:
    def __init__(self, size):
        self.memory = SharedMemory()
        self.agents = [Agent() for _ in range(size)]

    def step(self, world):
        for a in self.agents:
            a.act(world, self.memory)
        self.selection()
