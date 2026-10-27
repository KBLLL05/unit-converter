import pytest
from weight import kg_to_g, g_to_kg, kg_to_lb, lb_to_kg


def test_kg_to_g():
    assert kg_to_g(2) == 2000


def test_g_to_kg():
    assert g_to_kg(500) == 0.5


def test_kg_to_lb():
    assert kg_to_lb(1) == pytest.approx(2.20462, rel=1e-5)


def test_lb_to_kg():
    assert lb_to_kg(2.20462262185) == pytest.approx(1)


def test_zero_weight():
    assert kg_to_g(0) == 0


def test_negative_weight():
    with pytest.raises(ValueError):
        kg_to_g(-5)

@pytest.mark.parametrize(
    "invalid_weight",
    [True, "abc", float("nan"), float("inf")]
)
def test_invalid_inputs(invalid_weight):
    with pytest.raises(ValueError):
        kg_to_g(invalid_weight)
        