"""Module for all my transformation functions
"""
import numpy as np
from kinematics import attitude

def lvlh2pqw():
    pass

def pqw2lvlh():
    pass

def pqw2eci(raan, argp, inc):
    r"""Return rotation matrix to go from PQW to ECI

    Returns the rotation matrix to transform a vector represented in the perifocal
    frame to the inertial frame.

    Parameters
    ----------
    raan : float 
        Right ascension of the ascending node in radians
    argp : float
        Argument of periapsis in radians
    inc : float
        inclination of orbit in radians

    Returns
    -------
    PQW2ECI : ndarray
        3x3 numpy array defining the rotation matrix

    Author
    ------
    Shankar Kulumani		GWU		skulumani@gwu.edu
    """
    PQW2ECI = attitude.rot3(raan).dot(attitude.rot1(inc)).dot(attitude.rot3(argp))
    print(PQW2ECI)
    return PQW2ECI

def eci2pqw():
    pass

