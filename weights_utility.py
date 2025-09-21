import json

def load_weights():
    loadedWeights = {}
    try:
        with open("weights.json", "r") as f:
            loadedWeights = json.load(f)
    except Exception as e:
        print("Error while loading the weights")
        raise e
    weight_tupil = (loadedWeights['rooms'], loadedWeights['sqft'], loadedWeights['bais'])
    return weight_tupil

def save_weights(weight):
    try:
        with open("weights.json", "w") as f:
            json.dump(weight, f)
    except Exception as e:
        print("Error while loading the trained weights")
        raise e

def reset_weights():
    try:
        with open("weights.json", "w") as f:
            json.dump({"rooms": 0.1, "sqft": 0.1, "bais": 0.1},f)
    except Exception as e:
        print("Error while resetting the weight")
        raise e
    
def weights():
    try:
        with open("weights.json", "r") as f:
            weights = json.load(f)
            return weights
    except Exception as e:
        print("Failed to get the weights")
        raise e
