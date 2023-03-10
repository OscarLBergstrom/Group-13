import pytest
import numpy as np
import pdb
from decide import *


#########
# Decide Function
#########


def test_decide_true():
    numpoints = 30
    points = [[1, 1], [2, 2], [3, 3], [5, 5], [6, 6], [7, 7], [1, 2], [2, 3],
              [3, 4], [0, 0], [0, 0], [15, 15], [1, 1], [
                  0, 0], [0, 10], [20, 0], [1, 0], [2, 3],
              [0, 1], [1, 1], [-1, -1], [-1, 1], [0, 0], [0, 1], [0, 0], [3, 3], [1, -1], [0, 0], [3, 3], [0, 0]]
    lcm = np.ones((15, 15))  # 0=NOTUSED, 1=ANDD, 2=ORR
    puv = np.ones(15)

    parameters = {
        # Inpus to the Decide()-function
        "LENGTH1": 1,  # LICS 0,7,12
        "RADIUS1": 1,  # LICS 1,8,13
        "EPSILON": 1,  # Deviation from PI LIC 2,9
        "AREA1": 90,  # LICS 3,10,14
        "Q_PTS": 3,  # Number of concecutive points LIC 4
        "QUADS": 2,  # Number of concecutive in LIC 4
        "DIST": 3,  # Distance in LIC 6
        "N_PTS": 3,  # Number of concecutive points in LIC 6
        "K_PTS": 1,  # No. of int. pts. in LICs 7 , 12
        "A_PTS": 1,  # No. of int. pts. in LICs 8 , 13
        "B_PTS": 1,  # No. of int. pts. in LICs 8 , 13
        "C_PTS": 1,  # No. of int. pts. in LIC 9
        "D_PTS": 1,  # No. of int. pts. in LIC 9
        "E_PTS": 1,  # Number of integer points in LICs 10, 14
        "F_PTS": 1,  # Number of integer points in LICs 10, 14
        "G_PTS": 1,  # Number of integer points in LIC 11
        "LENGTH2": 1,  # Maximum lenght in LIC 12
        "RADIUS2": 1,  # Maximum lenght in LIC 13
        "AREA2": 1,  # Maximum area in LIC 14
    }

    assert decide(points, numpoints, parameters, lcm, puv) == 'YES'


def test_decide_false():
    numpoints = 12
    points = [[1, 1], [2, 2], [3, 3], [5, 5], [6, 6], [7, 7],
              [1, 2], [2, 3], [3, 4], [0, 0], [0, 0], [15, 15]]

    lcm = np.ones((15, 15))  # 0=NOTUSED, 1=ANDD, 2=ORR
    puv = np.ones(15)

    parameters = {
        # Inpus to the Decide()-function
        "LENGTH1": 1,  # LICS 0,7,12
        "RADIUS1": 1,  # LICS 1,8,13
        "EPSILON": 1,  # Deviation from PI LIC 2,9
        "AREA1": 1,  # LICS 3,10,14
        "Q_PTS": 1,  # Number of concecutive points LIC 4
        "QUADS": 1,  # Number of concecutive in LIC 4
        "DIST": 1,  # Distance in LIC 6
        "N_PTS": 1,  # Number of concecutive points in LIC 6
        "K_PTS": 1,  # No. of int. pts. in LICs 7 , 12
        "A_PTS": 1,  # No. of int. pts. in LICs 8 , 13
        "B_PTS": 1,  # No. of int. pts. in LICs 8 , 13
        "C_PTS": 1,  # No. of int. pts. in LIC 9
        "D_PTS": 1,  # No. of int. pts. in LIC 9
        "E_PTS": 1,  # Number of integer points in LICs 10, 14
        "F_PTS": 1,  # Number of integer points in LICs 10, 14
        "G_PTS": 1,  # Number of integer points in LIC 11
        "LENGTH2": 1,  # Maximum lenght in LIC 12
        "RADIUS2": 1,  # Maximum lenght in LIC 13
        "AREA2": 1,  # Maximum area in LIC 14
    }

    assert decide(points, numpoints, parameters, lcm, puv) == 'NO'


#########
# PUM
#########


def test_pum_correct():
    lcm = np.zeros((15, 15))  # Testing the example from the specifications
    lcm[0:4, 0:4] = [[1, 1, 2, 1], [1, 1, 2, 2], [2, 2, 1, 1], [1, 2, 1, 1]]
    cmv = np.array([False, True, True, True, False, False, False,
                    False, False, False, False, False, False, False, False])
    result_pum = pum(cmv, lcm)
    expected_pum = np.ones((15, 15))
    expected_pum[0:4, 0:4] = [[0, 0, 1, 0], [
        0, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]

    for i in range(15):  # setting the diagonal to 0
        for j in range(15):
            if i == j:
                expected_pum[i][j] = 0

    assert np.array_equal(expected_pum, result_pum)


#########
# FUV
#########


def test_fuv_correct():
    pum = np.ones((15, 15))
    pum[0:4, 0:4] = [[0, 0, 1, 0], [0, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]

    for i in range(15):  # setting the diagonal to 0
        for j in range(15):
            if i == j:
                pum[i][j] = 0
    puv = np.ones(15)
    puv[1] = False
    puv[3] = False
    puv[5] = False
    result_fuv = fuv(pum, puv)
    excepted_fuv = np.ones(15)
    excepted_fuv[0] = False
    assert np.array_equal(result_fuv, excepted_fuv)


#########
# LIC0
#########


def test_lic0_true():
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 1
    }
    assert lic0(points, numpoints, parameters['LENGTH1']) == True


def test_lic0_false():
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
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
    assert lic1(points, numpoints, parameters) == True


def test_lic1Invalid():
    numpoints = 3
    parameters["RADIUS1"] = -1  # Invalid radius input
    points = np.array([[1, 2], [2, 3], [3, 4]])
    assert lic1(points, numpoints, parameters) == False


def test_lic1Contained():
    numpoints = 3
    parameters["RADIUS1"] = 12
    points = np.array([[1, 2], [2, 3], [3, 4]])  # Can be contained
    assert lic1(points, numpoints, parameters) == False


#########
# LIC2
#########


def test_lic2():
    parameters["EPSILON"] = 0.1
    points = np.array([[4, 6], [6, 4], [4, 4]])  # 45 degrees is < pi - epsilon
    numpoints = 3
    assert lic2(points, numpoints, parameters)

    parameters["EPSILON"] = math.pi / 2  # >90 degrees is > pi - epsilon
    points = np.array([[2, 2], [4, 2], [5, 4]])
    numpoints = 3
    assert not lic2(points, numpoints, parameters)

    # one point coincides with vertex
    points = np.array([[4, 1], [2, 2], [2, 2]])
    assert not lic2(points, numpoints, parameters)

    # one point coincides with vertex
    points = np.array([[2, 2], [2, 2], [3, 1]])
    assert not lic2(points, numpoints, parameters)


def test_lic2_invalid_data():

    parameters["EPSILON"] = math.pi + 0.1       # epsilon > pi
    points = np.array([[4, 6], [6, 4], [4, 4]])
    numpoints = 3
    assert not lic2(points, numpoints, parameters)

#########
# LIC3
#########


def test_lic3_false():
    parameters["AREA1"] = 100
    # Should result in a triangle equal but not greater to 100
    points = [[1, 1], [0, 0], [0, 10], [20, 0], [1, 0], [2, 3]]
    value = lic3(points, len(points), parameters)

    assert value == False


def test_lic3_true():
    parameters["AREA1"] = 90
    # Should result in a triangle equal but not greater to 100
    points = [[1, 1], [0, 0], [0, 10], [20, 0], [1, 0], [2, 3]]
    value = lic3(points, len(points), parameters)

    assert value == True


def test_lic3_line():
    parameters["AREA1"] = 1
    points = [[1, 1], [2, 2], [3, 3]]
    value = lic3(points, len(points), parameters)

    assert value == False


#########
# LIC4
#########


def test_lic4_positive():  # tests if positive when data satisfies the condition
    parameters["QUADS"] = 2
    parameters["Q_PTS"] = 3

    points = np.array([[0, 1], [1, 1], [-1, -1], [-1, 1]])
    numpoints = 4

    assert lic4(points, numpoints, parameters)


def test_lic4_ambiguous_cond():  # tests if function properly assigns quadrants based on their ordering when a point has "ambiguous coordinates"
    parameters["QUADS"] = 2
    parameters["Q_PTS"] = 3

    points = np.array([[0, 0], [1, -1], [0, -1]])
    numpoints = 3

    assert lic4(points, numpoints, parameters)


def test_lic4_negative():  # tests if negative when data doesn't satisfy the condition
    parameters["QUADS"] = 4
    parameters["Q_PTS"] = 3

    points = np.array([[0, 1], [1, 1], [-1, -1], [-1, 1]])
    numpoints = 4

    assert not lic4(points, numpoints, parameters)


def test_lic4_invalid_data():
    parameters["QUADS"] = 4
    parameters["Q_PTS"] = 5     # Q_PTS > numpoints

    points = np.array([[0, 1], [1, 1], [-1, -1], [-1, 1]])
    numpoints = 4

    assert not lic2(points, numpoints, parameters)

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
# LIC6
#########

# Tests a valid case


def test_lic6_true1():
    parameters = {
        "DIST": 3,
        "N_PTS": 3
    }
    numpoints = 5
    points = np.array([[0, 0], [0, 1], [0, 0], [3, 3], [1, -1]])
    assert lic6(points, numpoints, parameters)


# Tests that it works even if start and end point's are the same point


def test_lic6_true2():
    parameters = {
        "DIST": 3,
        "N_PTS": 3
    }
    numpoints = 3
    points = np.array([[0, 0], [3, 3], [0, 0]])
    assert lic6(points, numpoints, parameters)


# Tests that it fails if N_PTS < 3


def test_lic6_false1():
    parameters = {
        "DIST": 3,
        "N_PTS": 2
    }
    numpoints = 5
    points = np.array([[0, 0], [0, 1], [0, 0], [3, 3], [1, -1]])
    assert not lic6(points, numpoints, parameters)


# Test that it fails if no points are far enough away


def test_lic6_false2():
    parameters = {
        "DIST": 3,
        "N_PTS": 3
    }
    numpoints = 5
    points = np.array([[0, 0], [0, 1], [0, 0], [1, 1], [1, -1]])
    assert not lic6(points, numpoints, parameters)


# Tests that it fails even if start and end point's are the same point


def test_lic6_true2():
    def test_lic6_true():
        parameters = {
            "DIST": 3,
            "N_PTS": 3
        }
        numpoints = 3
        points = np.array([[0, 0], [1, 1], [0, 0]])
        assert not lic6(points, numpoints, parameters)


#########
# LIC7
#########


def test_lic7_true():
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 1
    }
    k_pts = 2
    assert lic7(points, numpoints, parameters['LENGTH1'], k_pts) == True


def test_lic7_false():
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
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
    assert lic8(points, numpoints, parameters) == True


# Checking if these points can contain in a circle with radius 3


def test_lic8Valid2():
    parameters["A_PTS"] = 2
    parameters["B_PTS"] = 3
    parameters["RADIUS1"] = 10
    numpoints = 8
    points = np.array([[0, 2], [1, 2], [1.5, 3], [2, 4], [
        2.5, 3.5], [3, 3], [3.5, 2.5], [5, 4]])
    assert lic8(points, numpoints, parameters) == False


# Checking (a_pts+b_pts) > (numpoints-3)


def test_lic8Invalid1():
    parameters["A_PTS"] = 5
    parameters["B_PTS"] = 7
    numpoints = 10
    points = np.array([[1, 2], [2, 3], [3, 4]])
    assert lic8(points, numpoints, parameters) == False


# Checking (numpoints < 5)


def test_lic8Invalid2():
    parameters["A_PTS"] = 0
    parameters["B_PTS"] = 0
    numpoints = 4
    points = np.array([[1, 2], [2, 3], [3, 4]])
    assert lic8(points, numpoints, parameters) == False


# Checking that it fails when A_PTS < 1


def test_lic8Invalid3():
    parameters["A_PTS"] = 0
    parameters["B_PTS"] = 3
    parameters["RADIUS1"] = 10
    numpoints = 6
    points = np.array([[0, 2], [2, 4], [
        2.5, 3.5], [3, 3], [3.5, 2.5], [5, 4]])
    assert lic8(points, numpoints, parameters) == False


#########
# LIC9
#########


def test_lic9_positive_1():  # test if it returns True when data satisfies the condition
    parameters["EPSILON"] = 0.1
    parameters["C_PTS"] = 2
    parameters["D_PTS"] = 3
    points = np.array([[4, 6], [0, 0], [0, 0], [6, 4],
                       [0, 0], [0, 0], [0, 0], [4, 4]])
    numpoints = 8

    assert lic9(points, numpoints, parameters)


def test_lic9_positive_2():  # same test with negative coordinates
    parameters["EPSILON"] = 0.1
    parameters["C_PTS"] = 1
    parameters["D_PTS"] = 1

    points = np.array([[-4, -6], [1, 2], [-2, -4], [3, -1], [-4, -4]])
    numpoints = 5

    assert lic9(points, numpoints, parameters)


def test_lic9_positive_3():  # test where the set is somewhere in the middle of the array instead

    parameters["EPSILON"] = 0.1
    parameters["C_PTS"] = 1
    parameters["D_PTS"] = 1

    points = np.array([[0, 0], [0, 0], [2, 2], [0, 0], [
        4, 2], [0, 0], [5, 4], [1, 0]])
    numpoints = 8

    assert lic2(points, numpoints, parameters)


def test_lic9_negative_1():  # test when the angle is less than pi + epsilon and larger than pi - epsilon
    parameters["EPSILON"] = math.pi / 2
    parameters["C_PTS"] = 1
    parameters["D_PTS"] = 1

    # pi/2 < ~116 degrees < pi + pi/2
    points = np.array([[2, 2], [0, 0], [4, 2], [0, 0], [5, 4]])
    numpoints = 5

    assert not lic9(points, numpoints, parameters)


def test_lic9_invalid_data1():   # test when C_PTS + D_PTS > numpoints - 3
    parameters["EPSILON"] = math.pi / 2
    parameters["C_PTS"] = 2
    parameters["D_PTS"] = 2

    points = np.array([[2, 2], [0, 0], [4, 2], [0, 0], [5, 4]])
    numpoints = 5

    assert not lic9(points, numpoints, parameters)

def test_lic9_invalid_data2():   # test when numpoints < 5
    parameters["EPSILON"] = math.pi / 2
    parameters["C_PTS"] = 1
    parameters["D_PTS"] = 1

    points = np.array([[2, 2], [0, 0], [4, 2], [0, 0]])
    numpoints = 4

    assert not lic9(points, numpoints, parameters)

#########
# LIC10
#########


def test_lic10_unit_true():
    parameters["AREA1"] = 90
    parameters["E_PTS"] = 2
    parameters["F_PTS"] = 3
    points = [[10, 10], [0, 0], [10, 10], [10, 10], [
        0, 10], [10, 10], [10, 20], [10, 10], [20, 0]]
    value = lic10(points, len(points), parameters)

    assert value == True


def test_lic10_unit_false():
    parameters["AREA1"] = 90
    parameters["E_PTS"] = 2
    parameters["F_PTS"] = 3
    points = [[10, 10], [0, 0], [10, 10], [10, 10], [
        0, 0], [0, 10], [10, 10], [10, 10], [20, 10]]
    value = lic10(points, len(points), parameters)

    assert value == False


def test_lic10_unit_invalid(): # Test that it returns False if there are less than 5 points
    parameters["AREA1"] = 90
    parameters["E_PTS"] = 2
    parameters["F_PTS"] = 3
    points = [[10, 10], [0, 0], [10, 10]]
    value = lic10(points, len(points), parameters)

    assert value == False

#########
# LIC11
#########

def test_lic11_true(): #Tests a test case which should return True
    nrpoints = 5
    points = np.array([[0, 0], [4, 3], [1, 2], [2, 3], [3, 4], ])
    parameters = {"G_PTS": 2}
    assert lic11(nrpoints, points, parameters)


def test_lic11_false(): #Tests a test case which should return false
    nrpoints = 5
    parameters = {"G_PTS": 2}
    points = np.array([[0, 0], [1, 2], [2, 3], [3, 3], [3, 4]])
    assert not lic11(nrpoints, points, parameters)


def test_lic11_invalid(): #Test that it returns false if numpoints < 2
    numpoints = 2
    points = np.array([[4, 3], [3, 4]])
    parameters = {"G_PTS": 1}
    assert not lic11(numpoints, points, parameters)

#########
# LIC12
#########

def test_lic12_true():
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 1,
        "LENGTH2": 3
    }
    k_pts = 2
    assert lic12(points, numpoints,
                 parameters['LENGTH1'], parameters['LENGTH2'], k_pts) == True


def test_lic12_false1():
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 1,
        "LENGTH2": 1
    }
    k_pts = 2
    assert lic12(points, numpoints,
                 parameters['LENGTH1'], parameters['LENGTH2'], k_pts) == False


def test_lic12_false2():
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 5,
        "LENGTH2": 3
    }
    k_pts = 2
    assert lic12(points, numpoints,
                 parameters['LENGTH1'], parameters['LENGTH2'], k_pts) == False


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
    assert lic13(points, numpoints, parameters) == True


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
    assert lic13(points, numpoints, parameters) == False


# Checking that the program is false when radius2 = 0


def test_lic13Invalid1():
    parameters["RADIUS2"] = 0
    numpoints = 10
    points = np.array([[1, 2], [2, 3], [3, 4]])
    assert lic13(points, numpoints, parameters) == False


# Checking (numpoints < 5)


def test_lic13Invalid2():
    numpoints = 4
    points = np.array([[1, 2], [2, 3], [3, 4]])
    assert lic13(points, numpoints, parameters) == False


#########
# LIC14
#########


def test_lic14_unit_false():
    parameters["AREA1"] = 120
    parameters["AREA2"] = 80
    parameters["E_PTS"] = 2
    parameters["F_PTS"] = 3
    points = [[10, 10], [0, 0], [10, 10], [10, 10], [
        0, 0], [0, 10], [10, 10], [10, 10], [20, 10]]
    assert lic14(points, len(points), parameters) == False


def test_lic14_unit_true():
    parameters["AREA1"] = 90
    parameters["AREA2"] = 110
    parameters["E_PTS"] = 2
    parameters["F_PTS"] = 3
    points = [[10, 10], [0, 0], [10, 10], [10, 10], [
        0, 10], [10, 10], [10, 20], [10, 10], [20, 0]]
    assert lic14(points, len(points), parameters) == True


def test_lic14_unit_invalid(): # Test that it returns False if there are less than 5 points
    parameters["AREA1"] = 90
    parameters["AREA2"] = 110
    parameters["E_PTS"] = 2
    parameters["F_PTS"] = 3
    points = [[10, 10], [0, 0], [10, 10]]
    assert lic14(points, len(points), parameters) == False


#########
# Helper Function: Min Distance
#########


def test_min_distance_true():
    length = 2
    assert min_distance([1, 1], [3, 3], length) == True


def test_min_distance_false():
    length = 1
    assert min_distance([1, 1], [1, 1], length) == False


#########
# Helper Function: Max Distance
#########


def test_max_distance_true():
    length = 2
    assert max_distance([1, 1], [3, 3], length) == False


def test_max_distance_false():
    length = 1
    assert max_distance([1, 1], [1, 1], length) == True


#########
# Helper Function: Is Triangle
#########


def test_isTriangle():
    assert isTriangle([2, 2], [5, 5], [8, 2]) == True


def test_isNotTriangle():
    assert isTriangle([1, 2], [1, 3], [1, 4]) == False


#########
# Helper Function: Project
#########

def test_project():
    assert np.array_equal(
        project(np.array([-1, 1, 0]), np.array([-2, -1, 0])), [-1 / 2, 1 / 2, 0])
