import pytest
import numpy as np
from decide import *

#########
# LIC0
#########

def test_lic0_true():
    points = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 1
    }
    assert lic0(points, numpoints, parameters['LENGTH1']) == True

def test_lic0_false():
    points = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 2
    }
    assert lic0(points, numpoints, parameters['LENGTH1']) == False

#########
# LIC1
#########

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

#########
# LIC3
#########

def test_lic3_false():
    parameters["AREA1"] = 100
    points = [[1,1], [0,0], [0,10],[20,0],[1,0],[2,3]] # Should result in a triangle equal but not greater to 100
    value = lic3(points,len(points))

    assert value == False

def test_lic3_true():
    parameters["AREA1"] = 90
    points = [[1,1], [0,0], [0,10],[20,0],[1,0],[2,3]] # Should result in a triangle equal but not greater to 100
    value = lic3(points,len(points))

    assert value == True

def test_lic3_line():
    parameters["AREA1"] = 1
    points = [[1,1],[2,2],[3,3]]
    value = lic3(points,len(points))

    assert value == False

#########
# LIC4
#########


def test_lic4_positive():       # tests if positive when data satisfies the condition
    parameters["QUADS"] = 2
    parameters["Q_PTS"] = 3

    points = np.array([[0, 1], [1, 1], [-1, -1], [-1, 1]])
    numpoints = 4

    assert lic4(points, numpoints)


def test_lic4_ambiguous_cond():  # tests if function properly assigns quadrants based on their ordering when a point has "ambiguous coordinates"
    parameters["QUADS"] = 2
    parameters["Q_PTS"] = 3

    points = np.array([[0, 0], [1, -1], [0, -1]])
    numpoints = 3

    assert lic4(points, numpoints)


def test_lic4_negative():       # tests if negative when data doesn't satisfy the condition
    parameters["QUADS"] = 4
    parameters["Q_PTS"] = 3

    points = np.array([[0, 1], [1, 1], [-1, -1], [-1, 1]])
    numpoints = 4

    assert not lic4(points, numpoints)

#########
# LIC5
#########

def test_lic5_true():
    nrpoints = 5
    points = np.array([[0, 0], [1, 2], [2, 3], [4, 3], [3, 4]])
    assert lic5(nrpoints, points)

def test_lic5_false():
    nrpoints = 5
    points = np.array([[0, 0], [1, 2], [2, 3], [3, 3], [3, 4]])
    assert not lic5(nrpoints, points)

#########
# LIC7
#########

def test_lic7_true():
    points = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 1
    }
    k_pts = 2
    assert lic7(points, numpoints, parameters['LENGTH1'], k_pts) == True

def test_lic7_false():
    points = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 5
    }
    k_pts = 2
    assert lic7(points, numpoints, parameters['LENGTH1'], k_pts) == False

#########
# LIC8
#########

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

#########
# LIC12
#########

def test_lic12_true():
    points = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 1,
        "LENGTH2": 3
    }
    k_pts = 2
    assert lic12(points, numpoints, parameters['LENGTH1'], parameters['LENGTH2'], k_pts) == True

def test_lic12_false1():
    points = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 1,
        "LENGTH2": 1
    }
    k_pts = 2
    assert lic12(points, numpoints, parameters['LENGTH1'], parameters['LENGTH2'], k_pts) == False

def test_lic12_false2():
    points = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 5,
        "LENGTH2": 3
    }
    k_pts = 2
    assert lic12(points, numpoints, parameters['LENGTH1'], parameters['LENGTH2'], k_pts) == False

#########
# LIC13
#########

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

#########
# Helper Function: Min Distance
#########

def test_min_distance_true():
    length = 2
    assert min_distance([1,1],[3,3],length) == True

def test_min_distance_false():
    length = 1
    assert min_distance([1,1],[1,1],length) == False

#########
# Helper Function: Max Distance
#########

def test_max_distance_true():
    length = 2
    assert max_distance([1,1],[3,3],length) == False

def test_max_distance_false():
    length = 1
    assert max_distance([1,1],[1,1],length) == True

#########
# Helper Function: Is Triangle
#########

def test_isTriangle():

    assert isTriangle([2, 2], [5, 5], [8, 2]) == True


def test_lic1Invalid():
    numpoints = 3
    parameters["RADIUS1"] = -1  # Invalid radius input
    points = np.array([[1, 2], [2, 3], [3, 4]])
    assert lic1(points, numpoints) == False


def test_isNotTriangle():
    assert isTriangle([1, 2], [1, 3], [1, 4]) == False
