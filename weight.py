import math


def validate_weight(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Weight must be a number")

    if not math.isfinite(value):
        raise ValueError("Weight must be finite")

    if value < 0:
        raise ValueError("Weight cannot be negative")


def kg_to_g(kg):
    validate_weight(kg)
    return kg * 1000


def g_to_kg(g):
    validate_weight(g)
    return g / 1000


def kg_to_lb(kg):
    validate_weight(kg)
    return kg * 2.20462262185


def lb_to_kg(lb):
    validate_weight(lb)
    return lb / 2.20462262185