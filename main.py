from simulation.ecosystem import Ecosystem
from observer.gpt_observer import GPTObserver

eco = Ecosystem()
observer = GPTObserver()

for step in range(200):
    eco.step()

    if step % 10 == 0:
        report = observer.analyze(eco)
        prediction = observer.predict(report)

        print(f"Step {step}")
        print("Observed :", report)
        print("Predicted:", prediction)
from analysis.visualize import Visualizer

viz = Visualizer()

# dans la boucle
if step % 10 == 0:
    report = observer.analyze(eco)
    viz.record(report)

# après la boucle
viz.plot()
