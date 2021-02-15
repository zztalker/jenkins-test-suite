from contextlib import ExitStack
import pytest
import calculator as calc


@pytest.mark.parametrize('a, b, result', [
    pytest.param(1, 2, 3, id="add two positive int"),
    [1/3, 1/3, 2/3],
    [-1, 1, 0],
    [1, -1, 0],
    [0.5, 0.5, 1]
])
def test_add(a, b, result):
    assert calc.add(a, b) == result


@pytest.mark.parametrize('a, b, result, error', [
    [10, 5, 2, None],
    [10, 3, 10/3, None],
    [-10, 2, -5, None],
    [-10, -2, 5, None],
    [-10, 0, None, ZeroDivisionError],
])
def test_div(a, b, result, error):
    expectation = ExitStack() if error is None else pytest.raises(error)
    with expectation:
        assert calc.div(a, b) == result
