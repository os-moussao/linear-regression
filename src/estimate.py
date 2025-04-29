def estimate_price(mileage: float, a: float, b: float) -> int:
    return max(round(a * mileage + b), 0)

def main():
    a, b = 0., 0.
    try:
        with open("result.txt", "r") as file:
            a, b = map(float, file.read().split())
    except:
        print("\033[93mWarning: Model not trained yet.\033[0m")
        pass
    mileage = float(input("Enter the mileage of the car: "))
    print(f"Estimated price: {estimate_price(mileage, a, b)}")

if __name__ == "__main__":
    main()