"""Convert temperatures between Celsius and Fahrenheit.

Only finite int/float values at or above absolute zero are accepted.
"""

import math


def _validate_temperature(value, minimum):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("Temperature must be a number.")
    if not math.isfinite(value):
        raise ValueError("Temperature must be finite.")
    if value < minimum:
        raise ValueError("Temperature cannot be below absolute zero.")


def celsius_to_fahrenheit(celsius):
    """Return Fahrenheit for a Celsius temperature of at least -273.15."""
    _validate_temperature(celsius, -273.15)
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Return Celsius for a Fahrenheit temperature of at least -459.67."""
    _validate_temperature(fahrenheit, -459.67)
    return (fahrenheit - 32) * 5 / 9
