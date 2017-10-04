"""Kepler Module 2-body astrodynamics

"""

import numpy as np
from astro import constants

def specific_mechanical_energy(r, v, mu=constants.earth.mu):
    """Specific Mechanical Energy

    """
    energy = v**2 / 2 - mu / r
    return energy

def apoapsis_periapsis(a, ecc):
    """Compute radius of apoapsis and periapsis

    """
    rp = a * ( 1 -  ecc)
    ra = a * ( 1 + ecc)

    return ra, rp


