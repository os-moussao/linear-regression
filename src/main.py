import pandas as pd
from utils import std_scaling, standard_deviation, get_mean

learning_rate = 0.01

def estimate_price(mileage: int, a: float, b: float) -> float:
    return a * mileage + b

def gradient_descent(mileages: list[float], prices: list[float], a: float, b: float) -> tuple[float, float]:
    a_derivative, b_derivative = 0., 0.
    m = len(mileages)

    for mileage, price in zip(mileages, prices):
        estimated_price = estimate_price(mileage, a, b)
        a_derivative += (estimated_price - price) * mileage
        b_derivative += (estimated_price - price)

    a -= learning_rate * a_derivative / m
    b -= learning_rate * b_derivative / m

    return a, b

def train_model() -> tuple[float, float]:
    a, b = 0., 0.

    data = pd.read_csv("data.csv")
    x = data["km"].values
    x_scaled = std_scaling(x)
    y = data["price"].values

    for _ in range(1000):
        a, b = gradient_descent(x_scaled, y, a, b)

    std = standard_deviation(x)
    mean = get_mean(x)

    # unscale a and b
    a, b = a / std, b - a * mean / std

    return a, b

def main():
    a, b = train_model()
    mileage = float(input("Enter the mileage of the car: "))
    print(f"Estimated price: {estimate_price(mileage, a, b)}")

if __name__ == "__main__":
    main()