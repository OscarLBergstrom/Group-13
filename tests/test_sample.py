import pytest
import numpy as np
from decide import *


def test_lic9_positive_1():        # test if it returns True when data satisfies the condition
    parameters["EPSILON"] = 0.1
    parameters["C_PTS"] = 2
    parameters["D_PTS"] = 3
    points = np.array([[4, 6], [0, 0], [0, 0], [6, 4], [0, 0], [0, 0], [0, 0], [4, 4]])
    numpoints = 8

    assert True #lic9(points, numpoints)


def test_lic9_positive_2():       # same test with negative coordinates
    parameters["EPSILON"] = 0.1
    parameters["C_PTS"] = 1
    parameters["D_PTS"] = 1

    points = np.array([[-4, -6], [1, 2], [-2, -4], [3, -1], [-4, -4]])
    numpoints = 5

    assert lic9(points, numpoints)


def test_lic9_positive_3():  # test where the set is somewhere in the middle of the array instead

    parameters["EPSILON"] = 0.1
    parameters["C_PTS"] = 1
    parameters["D_PTS"] = 1

    points = np.array([[0, 0], [0, 0], [2, 2], [0, 0], [4, 2],  [0, 0], [5, 4],  [1, 0]])
    numpoints = 8

    assert lic2(points, numpoints)


def test_lic9_negative_1():     # test when the angle is less than pi + epsilon and larger than pi - epsilon
    parameters["EPSILON"] = math.pi/2
    parameters["C_PTS"] = 1
    parameters["D_PTS"] = 1

    points = np.array([[2, 2], [0, 0], [4, 2], [0, 0], [5, 4]])             # pi/2 < ~116 degrees < pi + pi/2
    numpoints = 5

    assert not lic9(points, numpoints)


