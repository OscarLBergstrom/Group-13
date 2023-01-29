from decide import *

def lic3_unit_test():
    parameters["AREA1"] = 100
    points = [[1,1], [0,0], [0,10],[20,0],[1,0],[2,3]] # Should result in a triangle equal but not greater to 100
    value = lic3(points,len(points))

    assert value == False

def lic3_line_test():
    parameters["AREA1"] = 1
    points = [[1,1],[2,2],[3,3]]
    value = lic3(points,len(points))

    assert value == False


if __name__ == '__main__':
    lic3_unit_test()
    lic3_line_test()
    
