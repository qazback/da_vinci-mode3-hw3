import pytest
from fuel import convert, gauge


def test_convert_valid_fraction():
    assert convert("3/4") == 75


def test_convert_invalid_fraction():
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_gauge_less_than_or_equal_to_1():
    assert gauge(1) == "E"
    assert gauge(0) == "E"


def test_gauge_greater_than_or_equal_to_99():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_other_values():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"


if __name__ == "__main__":
    pytest.main()
