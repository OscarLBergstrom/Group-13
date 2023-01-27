import pytest
import numpy as np
from decide import *
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

def test_lic2():
    parameters["EPSILON"] = 0.1
    points = np.array([[4,6],[6,4],[4,4]])        #45 degrees is < pi - epsilon
    numpoints = 3
    assert lic2(points, numpoints)

    parameters["EPSILON"] = math.pi/2              #>90 degrees is > pi - epsilon
    points = np.array([[2,2],[4,2],[5,4]])
    numpoints = 3
    assert not lic2(points, numpoints)

    points = np.array([[4,1],[2,2],[2,2]])        #one point coincides with vertex
    assert not lic2(points, numpoints)

    points = np.array([[2,2],[2,2],[3,1]])        #one point coincides with vertex
    assert not lic2(points, numpoints)