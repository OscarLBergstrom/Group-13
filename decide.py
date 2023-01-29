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

def lic3(points, numpoints):
    AREA = parameters["AREA1"]

    if numpoints < 3:
        return False
    
    for i in range(numpoints - 2):
        temp_area = herons_formula(points[i], points[i+1], points[i+2])
        print(temp_area)
        if(temp_area > AREA):
            return True
        
    return False

    
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

def lic10(points, numpoints):
    AREA = parameters["AREA1"]
    E_PTS = parameters["E_PTS"]
    F_PTS = parameters["F_PTS"]
    
    if(numpoints < 5):
        return False
    if(F_PTS + E_PTS > numpoints - 3):
        return False
    
    for i in range(numpoints - (F_PTS+E_PTS+2)):
        temp_area = herons_formula(points[i], points[i + E_PTS + 1], points[i + E_PTS + F_PTS + 2])
        if(temp_area > AREA):
            return True
        
    return False


def lic11():
    pass
    
def lic12():
    pass

def lic13():
    pass

def lic14(points, numpoints):
    AREA1 = parameters["AREA1"]
    AREA2 = parameters["AREA2"]
    E_PTS = parameters["E_PTS"]
    F_PTS = parameters["F_PTS"]

    if numpoints < 5:
        return False
    
    triangle_larger = False
    triangle_smaller = False

    for i in range(numpoints - (E_PTS+F_PTS+2)):
        temp_area = herons_formula(points[i], points[i + E_PTS + 1], points[i+ F_PTS + E_PTS + 2])
        
        if temp_area > AREA1:
            triangle_larger = True
        if temp_area < AREA2:
            triangle_smaller = True
        if triangle_smaller and triangle_larger:
            return True
    
    return False

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


if __name__ == '__main__':
    decide()