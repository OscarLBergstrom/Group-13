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

            elif points[j][0] >= 0 > points[j][1]:  # 4th quadrant
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



if __name__ == '__main__':
    print(decide())