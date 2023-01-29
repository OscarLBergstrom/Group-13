import pytest
import numpy as np
from decide import *


# Can not be contained = true
# can be contained = false

# Checking that the two conditions are being met and therefore true
def test_lic13Valid1():
    parameters["A_PTS"] = 2
    parameters["B_PTS"] = 3
    # points can not be contained in a circle with this radius
    parameters["RADIUS1"] = 1
    # points can be contained in a circle with this radius
    parameters["RADIUS2"] = 10
    numpoints = 8
    points = np.array([[0, 2], [1, 2], [1.5, 3], [2, 4], [
                      2.5, 3.5], [3, 3], [3.5, 2.5], [5, 4]])
    assert lic13(points, numpoints) == True


# Checking that the two conditions are not being met and therefore false
def test_lic13Valid2():
    parameters["A_PTS"] = 2
    parameters["B_PTS"] = 3
    # points can be contained in a circle with this radius
    parameters["RADIUS1"] = 10
    # points can be contained in a circle with this radius
    parameters["RADIUS2"] = 10
    numpoints = 8
    points = np.array([[0, 2], [1, 2], [1.5, 3], [2, 4], [
                      2.5, 3.5], [3, 3], [3.5, 2.5], [5, 4]])
    assert lic13(points, numpoints) == False

# Checking that the program is false when radius2 = 0


def test_lic13Invalid1():
    parameters["RADIUS2"] = 0
    numpoints = 10
    points = np.array([[1, 2], [2, 3], [3, 4]])
    assert lic13(points, numpoints) == False

#Checking (numpoints < 5)


def test_lic13Invalid2():
    numpoints = 4
    points = np.array([[1, 2], [2, 3], [3, 4]])
    assert lic13(points, numpoints) == False


if __name__ == '__main__':
    test_lic13Valid1()
    test_lic13Valid2()
    test_lic13Invalid1()
    test_lic13Invalid2()
