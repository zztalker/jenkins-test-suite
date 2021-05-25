import random
import time
import pytest


@pytest.mark.parametrize('a', [i for i in range(10)])
@pytest.mark.parametrize('b', [i for i in range(10)])
@pytest.mark.parametrize('c', [i for i in range(10)])
def test_add(a, b, c):
    time.sleep(random.random())
    assert random.random() <= 0.9
