import pytest
import numpy as np
from decide import *


def test_lic4_positive():       #tests if positive when data satisfies the condition
    parameters["QUADS"] = 2
    parameters["Q_PTS"] = 3

    points = np.array([[0, 1], [1, 1], [-1, -1], [-1, 1]])
    numpoints = 4

    assert lic4(points, numpoints)


def test_lic4_negative():       #tests if negative when data doesn't satisfy the condition
    parameters["QUADS"] = 4
    parameters["Q_PTS"] = 3

    points = np.array([[0, 1], [1, 1], [-1, -1], [-1, 1]])
    numpoints = 4

    assert not lic4(points, numpoints)

