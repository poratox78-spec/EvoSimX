class GPTObserver:
    def analyze(self, ecosystem):
        report = {}
        for k, pop in ecosystem.populations.items():
            report[k] = {
                "avg_fitness": pop.average_fitness(),
                "population": len(pop.agents)
            }
        return report

    def predict(self, report):
        return {
            k: v["avg_fitness"] * 1.05
            for k, v in report.items()
        }
def detect_patterns(self, history):
    trends = {}
    for k, values in history.items():
        if len(values) > 5:
            trends[k] = values[-1] - values[-5]
    return trends
    
