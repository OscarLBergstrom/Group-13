import pytest
import numpy as np
from decide import *


# Can not be contained = true
# can be contained = false

# Checking if these points cannot contain in a circle with radius 3
def test_lic8Valid1():
    parameters["A_PTS"] = 2
    parameters["B_PTS"] = 3
    parameters["RADIUS1"] = 3
    numpoints = 8
    points = np.array([[0, 2], [1, 2], [1.5, 3], [2, 4], [
                      2.5, 3.5], [3, 3], [3.5, 2.5], [5, 4]])
    assert lic8(points, numpoints) == True

# Checking if these points can contain in a circle with radius 3


def test_lic8Valid2():
    parameters["A_PTS"] = 2
    parameters["B_PTS"] = 3
    parameters["RADIUS1"] = 10
    numpoints = 8
    points = np.array([[0, 2], [1, 2], [1.5, 3], [2, 4], [
                      2.5, 3.5], [3, 3], [3.5, 2.5], [5, 4]])
    assert lic8(points, numpoints) == False


#Checking (a_pts+b_pts) > (numpoints-3)
def test_lic8Invalid1():
    parameters["A_PTS"] = 5
    parameters["B_PTS"] = 7
    numpoints = 10
    points = np.array([[1, 2], [2, 3], [3, 4]])
    assert lic8(points, numpoints) == False

#Checking (numpoints < 5)


def test_lic8Invalid2():
    parameters["A_PTS"] = 0
    parameters["B_PTS"] = 0
    numpoints = 4
    points = np.array([[1, 2], [2, 3], [3, 4]])
    assert lic8(points, numpoints) == False


# Checking that it fails when A_PTS < 1
def test_lic8Invalid3():
    parameters["A_PTS"] = 0
    parameters["B_PTS"] = 3
    parameters["RADIUS1"] = 10
    numpoints = 6
    points = np.array([[0, 2], [2, 4], [
                      2.5, 3.5], [3, 3], [3.5, 2.5], [5, 4]])
    assert lic8(points, numpoints) == False


if __name__ == '__main__':
    test_lic8Valid1()
    test_lic8Valid2()
    test_lic8Invalid1()
    test_lic8Invalid2()
