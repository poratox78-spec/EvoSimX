import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self):
        self.history = {"A": [], "B": [], "C": []}

    def record(self, report):
        for k in self.history:
            self.history[k].append(report[k]["avg_fitness"])

    def plot(self):
        for k, values in self.history.items():
            plt.plot(values, label=k)
        plt.legend()
        plt.xlabel("Time")
        plt.ylabel("Average fitness")
        plt.show()
      
