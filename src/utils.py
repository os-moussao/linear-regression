def get_mean(arr: list[float]) -> float:
    return sum(arr) / len(arr)

def standard_deviation(arr: list[float]) -> float:
    mean = get_mean(arr)
    variance = sum((x - mean) ** 2 for x in arr) / len(arr)
    return variance ** 0.5

def std_scaling(arr: list[float]) -> list[float]:
    mean = get_mean(arr)
    std = standard_deviation(arr)
    return [(x - mean) / std for x in arr]
