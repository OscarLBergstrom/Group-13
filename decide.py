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


def lic2():
    pass


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

    radius = parameters["LENGTH1"]
    # number of intervening points between two points
    a_pts = parameters["A_PTS"]
    # number of intervening points between two points
    b_pts = parameters["B_PTS"]

    if (numpoints < 5) or (a_pts < 1) or (b_pts < 1) or ((a_pts+b_pts) > (numpoints-3)):
        return False

    for i in range(len(points) - (a_pts+b_pts+2)):
        check = circleHelper(
            points[i], points[i+1+a_pts], points[i+2+a_pts+b_pts], radius)
        if check:
            return True

    return False


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


if __name__ == '__main__':
    print(decide())
