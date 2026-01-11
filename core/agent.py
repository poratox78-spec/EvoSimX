class Agent:
    def act(self, world, shared_memory):
        delta = world.signal() * 0.1
        self.energy += delta
        shared_memory.write(delta)
        self.energy += shared_memory.read() * 0.01
