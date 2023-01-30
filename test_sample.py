from decide import *
import pytest

def test_lic3_unit():
    parameters["AREA1"] = 100
    points = [[1,1], [0,0], [0,10],[20,0],[1,0],[2,3]] # Should result in a triangle equal but not greater to 100
    value = lic3(points,len(points))

    assert value == False

def test_lic3_line():
    parameters["AREA1"] = 1
    points = [[1,1],[2,2],[3,3]]
    value = lic3(points,len(points))

    assert value == False
  
