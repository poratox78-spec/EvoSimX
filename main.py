from core.population import Population
from simulation.world import World

def main():
    world = World()
    pop = Population(size=50)
    
    for step in range(100):
        pop.step(world)
        print(f"Step {step} | Avg fitness: {pop.average_fitness():.3f}")

if __name__ == "__main__":
    main()
