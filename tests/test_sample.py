import pytest
import numpy as np
from decide import *

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

def test_lic5():
    nrpoints=2
    points = np.array([[1,0],[0,2]])
    assert lic5(nrpoints, points)

    nrpoints=2
    points = np.array([[0,0],[0,2]])
    assert not lic5(nrpoints, points)

    nrpoints=2
    points = np.array([[0,0],[1,2]])
    assert not lic5(nrpoints, points)

    nrpoints=5
    points = np.array([[0, 0], [1, 2],[2,3],[3,3],[3,4]])
    assert not lic5(nrpoints, points)

    nrpoints = 5
    points = np.array([[0, 0], [1, 2], [2, 3], [4, 3], [3, 4]])
    assert lic5(nrpoints, points)