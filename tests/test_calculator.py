import sys

import pytest

from src.calculator import *


@pytest.mark.smoke
def test_add():
    assert add(2, 3) == 5


@pytest.mark.regression
def test_divide():
    assert divide(10, 2) == 5


@pytest.mark.regression
def test_divide_by_zero_raises_value_error_with_message():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert "Нельзя делить на ноль" in str(excinfo.value)


@pytest.mark.slow
def test_very_slow_calculation():
    """Гипотетический тест, который работает очень долго."""
    # для примера


@pytest.mark.skip(reason="Эта функциональность будет реализована в версии 2.0")
def test_subtraction():
    """Тест для будущей функции вычитания."""
    # assert subtract(10, 5) == 5
    pass

