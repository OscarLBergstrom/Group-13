import math
import numpy as np

PI = math.pi

NUMPOINTS = {}

# Input variables

numpoints = 0
points = np.zeros((numpoints, 2))
lcm = np.zeros((15, 15))  # 0=NOTUSED, 1=ANDD, 2=ORR
puv = np.zeros(15)

parameters = {
    # Inpus to the Decide()-function
    "LENGTH1": 0,     # LICS 0,7,12
    "RADIUS1": 0,     # LICS 1,8,13
    "EPSILON": 0,     # Deviation from PI LIC 2,9
    "AREA1": 0,       # LICS 3,10,14
    "Q_PTS": 0,       # Number of concecutive points LIC 4
    "QUADS": 0,       # Number of concecutive in LIC 4
    "DIST": 0,        # Distance in LIC 6
    "N_PTS": 0,       # Number of concecutive points in LIC 6
    "A_PTS": 0,       # No. of int. pts. in LICs 7 , 12
    "B_PTS": 0,       # No. of int. pts. in LICs 8 , 13
    "C_PTS": 0,       # No. of int. pts. in LIC 9
    "D_PTS": 0,       # No. of int. pts. in LIC 9
    "E_PTS": 0,  # Number of integer points in LICs 10, 14
    "F_PTS": 0,  # Number of integer points in LICs 10, 14
    "G_PTS": 0,  # Number of integer points in LIC 11
    "LENGTH2": 0,  # Maximum lenght in LIC 12
    "RADIUS": 0,  # Maximum lenght in LIC 13
    "AREA2": 0,  # Maximum area in LIC 14

}

def decide():
    pass

def cmv():
    pass

def pum(cmv_response):
    pass

def fuv(pum_response):
    pass


def lic0():
    pass

def lic1():
    pass

# There exists at least one set of three consecutive data points which form an angle such that:
# angle < (PI−EPSILON)
# or
# angle > (PI+EPSILON)
# The second of the three consecutive points is always the vertex of the angle. If either the first
# point or the last point (or both) coincides with the vertex, the angle is undefined and the LIC
# is not satisfied by those three points.
# (0 ≤ EPSILON < PI)

def lic2(points, numpoints):
    for i in range (1,numpoints-1):
        v = points[i]
        p1 = points[i-1]
        p2 = points[i+1]
        if(np.array_equal(v,p2) or np.array_equal(v,p1)):
            continue

        a = [v[0]-p1[0], v[1]-p1[1]]
        b = [v[0]-p2[0], v[1]-p2[1]]
        if angle(v, p1, p2) < PI - parameters["EPSILON"] or angle(v, p1, p2) > PI + parameters["EPSILON"]:
            return True
    return False

def angle(vertex, p1, p2):
    a = [vertex[0]-p1[0], vertex[1]-p1[1]]
    b = [vertex[0]-p2[0], vertex[1]-p2[1]]
    return np.arccos(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)))  #inverted dot product formula, angle in radians

def lic3():
    pass
    
def lic4():
    pass

def lic5():
    pass
    
def lic6():
    pass
    
def lic7():
    pass

def lic8():
    pass
    
def lic9():
    pass

def lic10():
    pass

def lic11():
    pass
    
def lic12():
    pass

def lic13():
    pass

def lic14():
    pass


if __name__ == '__main__':
    print(decide())