
import numpy as np
from code.practice import f

def test_f_scalar():
    assert f(2) == np.array([4])
    assert f(5) == np.array([25])


def test_f_array():
    assert f([2]) == np.array([4])
    assert f([5, 6, 7]) == np.array([25, 36, 49])
