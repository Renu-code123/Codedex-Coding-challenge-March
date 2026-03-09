## 🚀 Day 6 — Sputnik 9 Descent Simulation | Codédex Daily Challenge
def calculate_descent(altitude):
    layers = [
        (700, 10000, 2000),
        (85, 700, 500),
        (50, 85, 200),
        (12, 50, 75),
        (0, 12, 20)
    ]

    time = 0.0

    for low, high, rate in layers:
        if altitude > low:
            distance = min(altitude, high) - low
            time += (distance * 1000) / rate

    return round(time, 1)
