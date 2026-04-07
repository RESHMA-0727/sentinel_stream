import random

def predict_risk_ml(amount: float) -> float:
    """
    Fake ML model (simulates anomaly detection)
    """
    # higher amount → higher risk tendency
    base = amount / 10000

    # add randomness like real ML
    noise = random.uniform(0, 0.3)

    score = min(base + noise, 1.0)

    return round(score, 2)