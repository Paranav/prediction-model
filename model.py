import numpy as np
import pandas as pd
from weights_utility import load_weights, save_weights, reset_weights, weights




def train(csv_filename):
    df = pd.read_csv(csv_filename)
    diam = df[["rooms", "sqft"]].to_numpy(dtype=float)
    price = df["price"].to_numpy(dtype=float)

    w1, w2, bias = load_weights()

    lr = 0.00000001

    epochs = 1000

    for epoch in range(epochs):
        price_pred = w1*diam[:, 0] + w2*diam[:, 1] + bias
        error = price_pred - price

        dw1 = (2/len(diam)) * np.dot(error , diam[:,0])
        dw2 = (2/len(diam)) * np.dot(error, diam[:, 1])
        dbias = (2/len(diam)) * np.sum(error)

        w1 -= lr * dw1
        w2 -= lr * dw2

        bias -= lr * dbias

        if epoch % 100 == 0:
            loss = np.mean(error**2)
            print(f"Epoch {epoch}, Loss: {loss:.2f}, w1: {w1:.4f}, w2: {w2:.4f}, bias: {bias:.4f}")
            weights= {
                        "rooms": w1,
                        "sqft": w2,
                        "bais": bias
                    }
            save_weights(weights)


def predict_price(rooms, sqft):
    rooms_weight, sqft_weight, bias = load_weights()
    return rooms_weight*float(rooms) + sqft_weight*float(sqft) + bias


