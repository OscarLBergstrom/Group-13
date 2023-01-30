import math
import numpy as np
import pdb

PI = math.pi

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
    "K_PTS": 0,       # No. of int. pts. in LICs 7 , 12
    "A_PTS": 0,       # No. of int. pts. in LICs 8 , 13
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


def lic0(points, numpoints, length):
    if length < 0:
        False
    for i in range(0,numpoints-1):
        if (min_distance(points[i],points[i+1], length)):
            return True
    return False


def lic1():
    pass


def lic2(points, numpoints):
    for i in range (1,numpoints-1):
        v = points[i]
        p1 = points[i-1]
        p2 = points[i+1]
        if(np.array_equal(v,p2) or np.array_equal(v,p1)):
            continue

        if angle(v, p1, p2) < PI - parameters["EPSILON"] or angle(v, p1, p2) > PI + parameters["EPSILON"]:
            return True
    return False


def lic3():
    pass


def lic4():
    pass

def lic5(numpoints, points):
    for j  in range(1,numpoints):
        i = j-1
        if points[j][0]-points[i][0] < 0:
            return True
    return False
    
def lic6():
    pass

def lic7(points, numpoints, length, k_pts):
    if numpoints < 3 or length < 0:
        return False
    for i in range(0,numpoints-k_pts):
        if (min_distance(points[i],points[i+k_pts], length)):
            return True
    return False
    
def lic9(points, numpoints):
    if numpoints < 5:
        return False

    c = parameters["C_PTS"]
    d = parameters["D_PTS"]

    for i in range(0, numpoints):
        if i + d + c + 2 >= numpoints:
            break
        v = points[i+c+1]
        p1 = points[i]
        p2 = points[i+c+d+2]
        if np.array_equal(v, p2) or np.array_equal(v, p1):
            continue
        if angle(v, p1, p2) < (PI-parameters["EPSILON"]) or angle(v, p1, p2) > (PI + parameters["EPSILON"]):
            return True

    return False

def lic8(points, numpoints):

    # pdb.set_trace()
    radius = parameters["RADIUS1"]
    # number of intervening points between two points
    a_pts = parameters["A_PTS"]
    # number of intervening points between two points
    b_pts = parameters["B_PTS"]

    if (numpoints < 5) or (radius < 0) or (a_pts < 1) or (b_pts < 1) or ((a_pts+b_pts) > (numpoints-3)):
        return False

    for i in range(len(points) - (a_pts+b_pts+2)):
        if circleHelper(points[i], points[i+1+a_pts], points[i+2+a_pts+b_pts], radius):
            return True

    return False



def lic10():
    pass


def lic11():
    pass


def lic12(points, numpoints, length1, length2, k_pts):
    if numpoints < 3 or length2 < 0 or length1 < 0:
        return False

    cond1 = False
    cond2 = False

    for i in range(0,numpoints-k_pts):
        if not cond1 and (min_distance(points[i],points[i+k_pts], length1)):
            cond1 = True
        if not cond2 and (max_distance(points[i],points[i+k_pts], length2)):
            cond2 = True
        if cond2 and cond1:
            return True
    return False


def lic13():
    pass


def lic14():
    pass

if __name__ == '__main__':
    print(decide())

############# Helper functions ###############

def circleHelper(a, b, c, radius):

    # Distance from and to each of the points
    d1 = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    d2 = math.sqrt((c[0] - b[0])**2 + (c[1] - b[1])**2)
    d3 = math.sqrt((c[0] - a[0])**2 + (c[1] - a[1])**2)

    diameter = 2 * radius

    # Radius of the circumcircle that the three points create from a triangle
    # https://study.com/academy/lesson/circumradius-definition-formula.html

    # Check if the points form a triangle
    if isTriangle(a, b, c):
        # Radius of the circumcircle that the triangle form
        rCircumCircle = (d1*d2*d3)/(math.sqrt((d1 + d2 + d3) *
                                              (d2 + d3 - d1)*(d3 + d1 - d2)*(d1 + d2 - d3)))
        if rCircumCircle > radius:  # cannot be contained inside circle
            return True

    if d1 > diameter or d2 > diameter or d3 > diameter:
        return True

    else:
        return False

def isTriangle(a, b, c):
    # Calculate the distance between each pair of points
    d1 = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    d2 = math.sqrt((c[0] - b[0])**2 + (c[1] - b[1])**2)
    d3 = math.sqrt((c[0] - a[0])**2 + (c[1] - a[1])**2)

    # Check if the sum of any two sides of the triangle is greater than the third side
    if d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1:
        return True
    else:
        return False

def min_distance(point1,point2,length):
    if length < math.dist(point1,point2):
        return True
    return False

def max_distance(point1,point2,length):
    if length > math.dist(point1,point2):
        return True
    return False

def angle(vertex, p1, p2):
    a = [vertex[0]-p1[0], vertex[1]-p1[1]]
    b = [vertex[0]-p2[0], vertex[1]-p2[1]]
    return np.arccos(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)))  #inverted dot product formula, angle in radians