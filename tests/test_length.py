
import pytest

from length import (
    metres_to_kilometres,
    kilometres_to_metres,
    metres_to_miles,
    miles_to_metres,
    kilometres_to_miles,
    miles_to_kilometres,
)


def test_metres_to_kilometres():
    assert metres_to_kilometres(2500) == 2.5


def test_kilometres_to_metres():
    assert kilometres_to_metres(1.5) == 1500


def test_metres_to_miles():
    assert metres_to_miles(1609.344) == pytest.approx(1.0)


def test_miles_to_metres():
    assert miles_to_metres(1) == pytest.approx(1609.344)


def test_zero_length():
    assert metres_to_kilometres(0) == 0
    assert metres_to_miles(0) == 0


def test_kilometres_and_miles_round_trip():
    distance = 5
    assert miles_to_kilometres(kilometres_to_miles(distance)) == pytest.approx(distance)


def test_negative_length_is_rejected():
    with pytest.raises(ValueError):
        metres_to_kilometres(-1)


def test_non_numeric_length_is_rejected():
    with pytest.raises(ValueError):
        metres_to_miles("100")

