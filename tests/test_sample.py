import pytest
from decide import *
import pdb

def test_lic0_true():
    NUMPOINTS = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 1
    }
    assert lic0(NUMPOINTS, numpoints, parameters['LENGTH1']) == True

def test_lic0_false():
    NUMPOINTS = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]
    numpoints = 7
    parameters = {
        "LENGTH1": 2
    }
    assert lic0(NUMPOINTS, numpoints, parameters['LENGTH1']) == False

def test_min_distance_true():
    length = 2
    assert min_distance(1,1,3,3,length) == True

def test_min_distance_false():
    length = 1
    assert min_distance(1,1,1,1,length) == False

if __name__ == '__main__':
    test_lic0_false
    test_lic0_true
    test_min_distance_false
    test_lic0_true