import pytest
import numpy as np
from decide import *


# Can not be contained = true
# can be contained = false

def test_lic1NotContained():
    numpoints = 3
    parameters["RADIUS1"] = 0.5
    points = np.array([[-3, -2], [-2, -1], [-1, 0]])  # Can not be contained
    assert lic1(points, numpoints) == True


def test_lic1Contained():
    numpoints = 3
    parameters["RADIUS1"] = 12
    points = np.array([[1, 2], [2, 3], [3, 4]])  # Can be contained
    assert lic1(points, numpoints) == False


def test_isTriangle():

    assert isTriangle([2, 2], [5, 5], [8, 2]) == True


def test_lic1Invalid():
    numpoints = 3
    parameters["RADIUS1"] = -1  # Invalid radius input
    points = np.array([[1, 2], [2, 3], [3, 4]])
    assert lic1(points, numpoints) == False


def test_isNotTriangle():
    assert isTriangle([1, 2], [1, 3], [1, 4]) == False


if __name__ == '__main__':
    test_isNotTriangle()
    test_isTriangle()
    test_lic1Contained()
    test_lic1NotContained()
    test_lic1Invalid()
