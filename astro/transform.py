"""Module for all my transformation functions
"""
import numpy as np
from kinematics import attitude

def lvlh2pqw():
    pass

def pqw2lvlh():
    pass

def pqw2eci(raan, argp, inc):
    """Provide the rotation matrix to go from PQW to ECI
    
    Input:
    """
    PQW2ECI = attitude.rot3(raan).dot(attitude.rot1(inc)).dot(attitude.rot3(argp))
    return PQW2ECI

def eci2pqw():
    pass

