from simulation.ecosystem import Ecosystem
from observer.gpt_observer import GPTObserver
from analysis.visualize import Visualizer
from analysis.metrics import entropy, trend, average

# Création de l'écosystème
eco = Ecosystem()

# Observateur passif
observer = GPTObserver()

# Visualisation
viz = Visualizer()

# Nombre d'étapes de simulation
TOTAL_STEPS = 500  # tu peux augmenter à 5000+ pour observer l'évolution sur du long terme

for step in range(TOTAL_STEPS):
    # 1️⃣ Faire agir les populations
    eco.step()

    # 2️⃣ Observer tous les 10 pas
    if step % 10 == 0:
        report = observer.analyze(eco)
        prediction = observer.predict(report)

        # Affichage console
        print(f"Step {step}")
        print("Observed :", report)
        print("Predicted:", prediction)

        # Enregistrer pour visualisation
        viz.record(report)

# Afficher les courbes de fitness
viz.plot()

# Analyse automatique de diversité et de tendance sur les 3 populations
for pop_name, values in viz.history.items():
    avg_fitness = average(values)
    pop_entropy = entropy(values)
    pop_trend = trend(values, steps=5)

    # Imprimer les résultats pour chaque population
    print(f"\nPopulation {pop_name} - Statistiques")
    print(f"Average Fitness: {avg_fitness:.4f}")
    print(f"Diversity (Entropy): {pop_entropy:.4f}")
    print(f"Trend over last 5 steps: {pop_trend:.4f}")
# Analyse rapide de tendances (optionnelle)
trends = observer.detect_patterns(viz.history)
print("Trends sur les 5 derniers pas :", trends)
