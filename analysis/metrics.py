import numpy as np

def entropy(values):
    """
    Mesure de la diversité de la population.
    L'entropie est l'écart-type des valeurs.
    Plus l'entropie est élevée, plus la population est diverse.
    """
    return np.std(values)

def trend(values, steps=5):
    """
    Mesure de tendance sur les derniers 'steps' pas.
    Retourne la différence entre la valeur actuelle et la valeur d'il y a 'steps' pas.
    Une grande différence indique un changement rapide.
    """
    if len(values) < steps:
        return 0
    return values[-1] - values[-steps]

def average(values):
    """
    Moyenne des valeurs, peut être utilisé pour la fitness moyenne d'une population.
    """
    return np.mean(values)
  
