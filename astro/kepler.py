"""Kepler module for two-body astrodynamics

A collection of functions to perform astrodynamic computations for two
body orbital dynamics.

Attributes
----------
None

Author
------
Shankar Kulumani		GWU		skulumani@gwu.edu
"""
import numpy as np
from astro import constants

def specific_mechanical_energy(r, v, mu=constants.earth.mu):
    r"""Specific Mechanical Energy for keplerian orbit

    Compute the specific mechanical energy for a conic section.

    Parameters
    ----------
    r : float
        magnitude of relative position vector in km
    v : float
        magnitude of relative velocity vector in km
    mu : float
        gravitational paramter in km^3/sec^2

    Returns
    -------
    energy : float
        Specific mechanical energy in km^2/sec^2

    Other Parameters
    ----------------
    none

    Raises
    ------
    None

    See Also
    --------
    None

    Notes
    -----
    You may include some math:

    .. math:: \epsilon = \frac{v^2}{2} - \frac{\mu}{r}

    Author
    ------
    Shankar Kulumani		GWU		skulumani@gwu.edu

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] Bate, Mueller, White Fundamentals of Astrodynamics
    .. [2] MAE3145 GWU

    Examples
    --------
    An example of how to use the function

    >>> r = 1
    >>> v = 0
    >>> mu = 1
    >>> specific_mechanical_energy(r, v)
    -1.0
    """
    energy = v**2 / 2 - mu / r
    return energy

def apoapsis_periapsis(a, ecc):
    r"""Compute radius of apoapsis and periapsis for an elliptical orbit

    This computes apoapsis and periapsis. If you try this with an orbit with a large
    eccentricity, the apopasis number will not make any sense.

    Parameters
    ----------
    a : float
        semi-major axis in km
    ecc : float
        eccentricity unitless

    Returns
    -------
    ra : float
        Radius of apoapsis in km
    rp : float
        Raidus of periapsis in km

    Other Parameters
    ----------------
    None

    Raises
    ------
    None

    See Also
    --------
    None

    Author
    ------
    Shankar Kulumani		GWU		skulumani@gwu.edu

    References
    ----------

    .. [1] Bate, Mueller, White Fundamentals of Astrodynamics 

    Examples
    --------
    An example of how to use the function

    >>> a = 6378
    >>> ecc = 0
    >>> apoapsis_periapsis(a, ecc)
    (6378, 6378)
    """ 
    rp = a * ( 1 -  ecc)
    ra = a * ( 1 + ecc)

    return ra, rp


