class GPTObserver:
    def observe(self, population):
        return {
            "avg_fitness": population.average_fitness(),
            "population_size": len(population.agents)
        }
      
