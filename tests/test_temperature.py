"""Normal, boundary, and invalid-input tests for temperature conversion."""

import pytest

from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


@pytest.mark.parametrize("celsius, fahrenheit", [(0, 32), (100, 212), (-40, -40)])
def test_celsius_to_fahrenheit(celsius, fahrenheit):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(fahrenheit)


@pytest.mark.parametrize("fahrenheit, celsius", [(32, 0), (212, 100), (98.6, 37)])
def test_fahrenheit_to_celsius(fahrenheit, celsius):
    assert fahrenheit_to_celsius(fahrenheit) == pytest.approx(celsius)


def test_absolute_zero_is_allowed():
    assert celsius_to_fahrenheit(-273.15) == pytest.approx(-459.67)
    assert fahrenheit_to_celsius(-459.67) == pytest.approx(-273.15)


@pytest.mark.parametrize("convert, value", [
    (celsius_to_fahrenheit, -273.16),
    (fahrenheit_to_celsius, -459.68),
])
def test_below_absolute_zero_is_rejected(convert, value):
    with pytest.raises(ValueError, match="absolute zero"):
        convert(value)


@pytest.mark.parametrize("convert", [celsius_to_fahrenheit, fahrenheit_to_celsius])
@pytest.mark.parametrize("value", ["20", None, True])
def test_non_numeric_input_is_rejected(convert, value):
    with pytest.raises(TypeError, match="number"):
        convert(value)


@pytest.mark.parametrize("convert", [celsius_to_fahrenheit, fahrenheit_to_celsius])
@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_non_finite_input_is_rejected(convert, value):
    with pytest.raises(ValueError, match="finite"):
        convert(value)
