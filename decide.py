import math
import numpy as np

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

# Global variables declarations


def DECIDE(numpoints, points, parameters, lcm, puv):
    pass


def cmv(numpoints, points, parameters):
    # Calls the 15 LIC
    pass


def pum(lcm, cmv):
    pass


def fuv(puv, pum):
    pass


def lic0(parameters):
    pass


def lic1(parameters):
    pass


def lic2(parameters):
    pass


def lic3(parameters):
    pass


def lic4(parameters):
    pass


def lic5(parameters):
    pass


def lic6(parameters):
    pass


def lic7(parameters):
    pass


def lic8(parameters):
    pass


def lic9(parameters):
    pass


def lic10(parameters):
    pass


def lic11(parameters):
    pass


def lic12(parameters):
    pass


def lic13(parameters):
    pass


def lic14(parameters):
    pass


if __name__ == '__main__':
    DECIDE(numpoints, points, parameters, lcm, puv)
