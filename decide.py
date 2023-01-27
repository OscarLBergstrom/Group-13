import math
import numpy as np

PI = math.pi

NUMPOINTS = {}

POINTS = {}

PARAMETERS = {  
#Inpus to the Decide()-function
"LENGTH1" : 0,     # LICS 0,7,12
"RADIUS1" : 0,     # LICS 1,8,13
"EPSILON" : 0,     # Deviation from PI LIC 2,9
"AREA1" : 0,       # LICS 3,10,14
"Q_PTS" : 0,       # Number of concecutive points LIC 4
"QUADS" : 0,       # Number of concecutive in LIC 4
"DIST" : 0,        # Distance in LIC 6
"N_PTS" : 0,       # Number of concecutive points in LIC 6
"A_PTS" : 0,       # No. of int. pts. in LICs 7 , 12
"B_PTS" : 0,       # No. of int. pts. in LICs 8 , 13
"C_PTS" : 0,       # No. of int. pts. in LIC 9
"D_PTS" : 0,       # No. of int. pts. in LIC 9
"E_PTS" : 0,       #Number of integer points in LICs 10, 14
"F_PTS" : 0,       #Number of integer points in LICs 10, 14
"G_PTS" : 0,       #Number of integer points in LIC 11
"LENGTH2" : 0,     #Maximum lenght in LIC 12
"RADIUS" : 0,      #Maximum lenght in LIC 13
"AREA2" : 0,       #Maximum area in LIC 14
}
# Global variables declarations


def decide():
    fuv_response = fuv(pum(cmv()))

    for boolean in fuv_response:
        if not boolean:
            return 'NO'
    return 'YES'

def cmv():
    response = [lic0(),lic1(),lic2(),lic3(),lic4(),lic5(),lic6(),lic7(),lic8(),lic9(),lic10(),lic11(),lic12(),lic13(),lic14()]

    return response

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
    
