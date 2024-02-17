import random
import time
import pytest


@pytest.mark.parametrize('a', [i for i in range(3)])
@pytest.mark.parametrize('b', [i for i in range(3)])
@pytest.mark.parametrize('c', [i for i in range(3)])
def test_add(a, b, c):
    time.sleep(random.random()/100)
    assert random.random() <= 0.9


def test_new():
    assert False

