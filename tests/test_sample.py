import pytest
from decide import *
import pdb

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