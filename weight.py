def kg_to_g(kg):
    if kg < 0:
        raise ValueError("Weight cannot be negative")
    return kg * 1000


def g_to_kg(g):
    if g < 0:
        raise ValueError("Weight cannot be negative")
    return g / 1000


def kg_to_lb(kg):
    if kg < 0:
        raise ValueError("Weight cannot be negative")
    return kg * 2.20462262185


def lb_to_kg(lb):
    if lb < 0:
        raise ValueError("Weight cannot be negative")
    return lb / 2.20462262185