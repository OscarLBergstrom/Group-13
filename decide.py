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



def lic1(points, numpoints):

    radius = parameters["RADIUS1"]

    # If we dont even have 3 points or the radius is smaller than 0
    if (numpoints < 3) or (0 > radius):
        return False

    for i in range(len(points) - 2):
        check = circleHelper(points[i], points[i+1], points[i+2], radius)
        if check:  # If some point cannot be contained inside a circle
            return True

    return False



def lic2():
    pass

def lic3(points, numpoints):
    AREA = parameters["AREA1"]

    if numpoints < 3:
        return False
    
    for i in range(numpoints - 2):
        temp_area = herons_formula(points[i], points[i+1], points[i+2])
        if(temp_area > AREA):
            return True
        
    return False


def lic4(points, numpoints):
    
    q = parameters["Q_PTS"]
    quadrants = np.zeros(4)
    count = 0
    for i in range(0, numpoints-q+1):
        for j in range(i, i+q):
            if points[j][0] >= 0 <= points[j][1]:  # 1st quadrant
                if not quadrants[0]:
                    quadrants[0] = 1
                    count += 1

            elif points[j][0] > 0 > points[j][1]:  # 4th quadrant
                if not quadrants[3]:
                    quadrants[3] = 1
                    count += 1

            elif points[j][0] < 0 <= points[j][1]:  # 2nd quadrant
                if not quadrants[1]:
                    quadrants[1] = 1
                    count += 1

            else:                                   # 3rd quadrant
                if not quadrants[2]:
                    quadrants[2] = 1
                    count += 1
        if count > parameters["QUADS"]:
            return True
        count = 0
        quadrants[...] = 0
    return False


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


def lic9():
    pass


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

# Calculates the area of a triangle with the datapoints a,b,c. Used in Lic 3.
def herons_formula(a,b,c):
    len_1 = calculate_length(a,b)
    len_2 = calculate_length(a,c)
    len_3 = calculate_length(b,c)

    s = (len_1 + len_2 + len_3)/2

    area = math.sqrt(s*(s-len_1)*(s-len_2)*(s-len_3))

    return area

# Calculates the length between two datapoints a,b. Used in herons_formula (lic3).
def calculate_length(a,b):
    len = math.sqrt(pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2))
    return len


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
