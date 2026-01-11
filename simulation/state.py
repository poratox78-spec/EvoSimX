import pickle

def save(ecosystem, filename="state.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(ecosystem, f)

def load(filename="state.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)
      
