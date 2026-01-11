class SharedMemory:
    def __init__(self, size=100):
        self.buffer = []
        self.size = size

    def write(self, value):
        self.buffer.append(value)
        if len(self.buffer) > self.size:
            self.buffer.pop(0)

    def read(self):
        return sum(self.buffer)/len(self.buffer) if self.buffer else 0
