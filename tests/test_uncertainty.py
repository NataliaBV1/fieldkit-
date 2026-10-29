import pytest
from fieldkit.uncertainty import Measurement

def test_measurement_creation():
    m = Measurement(10.0, 0.5)
    assert m.value == 10.0
    assert m.uncertainty == 0.5

def test_negative_uncertainty_raises_error():
    with pytest.raises(ValueError):
        Measurement(10.0, -0.5)

def test_addition_propagation():
    m1 = Measurement(10.0, 0.3)
    m2 = Measurement(5.0, 0.4)
    res = m1 + m2
    assert res.value == 15.0
    # La incertidumbre combinada debe ser sqrt(0.3^2 + 0.4^2) = 0.5
    assert pytest.approx(res.uncertainty, 0.01) == 0.5
