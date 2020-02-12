import pytest
import calculator as calc


@pytest.mark.parametrize('a, b, result', [
    [1, 2, 3],
    [1/3, 1/3, 2/3],
    [-1, 1, 0],
    [0.5, 0.5, 1]
])
def test_add(a, b, result):
    assert calc.add(a, b) == result