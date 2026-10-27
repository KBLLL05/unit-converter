
"""Length conversion functions."""

METRES_PER_KILOMETRE = 1000
METRES_PER_MILE = 1609.344


def _validate_length(value):
    """Return a valid non-negative length or raise ValueError."""
    import math

    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Length must be a number.")

    if not math.isfinite(value) or value < 0:
        raise ValueError("Length must be finite and non-negative.")

    return value


def metres_to_kilometres(metres):
    return _validate_length(metres) / METRES_PER_KILOMETRE


def kilometres_to_metres(kilometres):
    return _validate_length(kilometres) * METRES_PER_KILOMETRE


def metres_to_miles(metres):
    return _validate_length(metres) / METRES_PER_MILE


def miles_to_metres(miles):
    return _validate_length(miles) * METRES_PER_MILE


def kilometres_to_miles(kilometres):
    return metres_to_miles(kilometres_to_metres(kilometres))


def miles_to_kilometres(miles):
    return metres_to_kilometres(miles_to_metres(miles))
