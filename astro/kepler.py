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
from kinematics import attitude

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

def rv2coe(r, v, mu):
    """Position and Velocity vectors to classical orbital elements

    ( p,a,ecc,inc,raan,arg_p,nu,m,arglat,truelon,lonper ) = rv2coe(r,v, mu)

    Inputs:
        - r - position vector in inertial frame (km)
        - v - velocity vector in inertial frame (km/sec)
        - mu - gravitational parameter of central body (km^3/sec^2)

    Outputs:
        - p - semi-major axis (km)
        - ecc - eccentricity
        - raan - right acsension of the ascending node (rad) 0 < raan <
        2*pi
        - inc - inclination (rad) 0 < inc < pi
        - arg_p - argument of periapsis (rad) 0 < arg_p < 2*pi
        - nu - true anomaly (rad) 0 < nu < 2*pi
        - m - mean anomaly in rad
        - arglat - argument of latitude(CI) rad 0 <arglat < 2*pi
        - truelon - true longitude (CE) rad 0 < truelon < 2*pi
        - lonper - longitude of periapsis rad 0 < lonper < 2*pi

    Dependencies:
        - numpy - everything is dependent on numpy
        - nu2anom - converts true anomaly to eccentric/mean anomaly

    Author:
        - Shankar Kulumani 30 Sept 2012
            - used old USAFA code and AAE532
        - Shankar Kulumani 5 September 2017
            - convert to Python for use in MAE3145

    References
        - AAE532 Notes
        - Vallado 3rd Edition
    """

    tol = 1e-9

    # calculate angular moemntum vector and magnitude
    mag_r = np.linalg.norm(r)
    mag_v = np.linalg.norm(v)

    rdotv = np.dot(r, v)

    h = np.cross(r, v)
    mag_h = np.linalg.norm(h)

    h_hat = h / mag_h
    # find n,e
    if mag_h > tol:
        n = np.zeros(3)
        n[0] = -h[1]
        n[1] = h[0]
        n[2] = 0.0

        with np.errstate(divide='raise'):
            try:
                mag_n = np.linalg.norm(n)
                n_hat = n / mag_n
            except FloatingPointError:
                mag_n = 0
                n_hat = np.zeros(3)

        # eccentricity vector
        e = ((mag_v**2 - mu / mag_r) * r - rdotv * v) / mu

        ecc = np.linalg.norm(e)
        mag_e = ecc

        sme = mag_v**2 / 2 - mu / mag_r

        if np.absolute(sme) > tol:
            a = -mu / (2 * sme)
        else:
            a = np.inf

        p = mag_h**2 / mu

        # inclination
        inc = np.arccos(h[2] / mag_h)

        # determine orbit type
        orbit_type = 'ei'
        if ecc < tol:
            # circular equatorial
            if inc < tol or np.absolute(inc - np.pi) < tol:
                orbit_type = 'ce'
            else:
                # circular inclined
                orbit_type = 'ci'

        else:
            #  elliptical, parabolic, hyperbolic equatorial -
            if inc < tol or np.absolute(inc - np.pi) < tol:
                orbit_type = 'ee'

        # right ascension of the ascending node
        if mag_n > tol:
            temp = n[0] / mag_n
            if np.absolute(temp) > 1.0:
                temp = np.sign(temp)
            raan = np.arccos(temp)
            if n[1] < 0.0:
                raan = 2 * np.pi - raan
        else:
            raan = 0

        # find argument of periapsis
        if orbit_type == 'ei':
            arg_p = np.arccos(np.dot(n, e) / (mag_n * mag_e))
            if e[2] < 0.0:
                arg_p = 2 * np.pi - arg_p
        else:
            arg_p = 0

        # ------------ find true anomaly at epoch - ------------
        if orbit_type[0] == 'e':
            nu = np.arccos(np.dot(e, r) / (mag_e * mag_r))
            if rdotv < 0.0:
                nu = 2 * np.pi - nu
        else:
            nu = 0

        # special orbit cases
        # ---- find argument of latitude - circular inclined - ----
        if orbit_type == 'ci':
            arglat = np.arccos(np.dot(n, r) / (mag_n * mag_r))
            if r[2] < 0.0:
                arglat = 2 * pi - arglat
            m = arglat
            nu = arglat
        else:
            arglat = 0

        # -- find longitude of perigee - elliptical equatorial - ---
        if ecc > tol and orbit_type == 'ee':
            temp = e[0] / ecc
            if np.absolute(temp) > 1.0:
                temp = np.sign(temp)
            lonper = np.arccos(temp)
            if e[1] < 0.0:
                lonper = 2 * pi - lonper
            if inc > pi / 2:
                lonper = 2 * pi - lonper

            arg_p = lonper
        else:
            lonper = 0

        # -------- find true longitude - circular equatorial - -----
        if mag_r > tol and orbit_type == 'ce':
            temp = r[0] / mag_r
            if np.absolute(temp) > 1.0:
                temp = np.sign(temp)
            truelon = np.arccos(temp)
            if r[1] < 0.0:
                truelon = 2 * np.pi - truelon
            if inc > np.pi / 2:
                truelon = 2 * np.pi - truelon
            m = truelon

            nu = truelon
        else:
            truelon = 0

        # find mean anomaly
        if orbit_type[0] == 'e':
            E, m = nu2anom(nu, ecc)
    else:
        p = 0
        a = 0
        ecc = 0
        inc = 0
        raan = 0
        arg_p = 0
        nu = 0
        m = 0
        arglat = 0
        truelon = 0
        lonper = 0

    return p, a, ecc, inc, raan, arg_p, nu, m, arglat, truelon, lonper

def nu2anom(nu, ecc):
    """Calculates the eccentric and mean anomaly given eccentricity and true
    anomaly

    ( E, M ) = ecc_anomaly(nu,ecc)

    Inputs:
        - nu - true anomaly in rad -2*pi < nu < 2*pi
        - ecc - eccentricity of orbit 0 < ecc < inf

    Outputs:
        - E - (elliptical/parabolic/hyperbolic) eccentric anomaly in rad
            0 < E < 2*pi
        - M - mean anomaly in rad 0 < M < 2*pi

    Dependencies:
        - numpy - everything is dependent on numpy
        - kinematics.attitude.normalize - normalize angles
    
    Notes
    -----
    This function is valid for all orbit types. 

    Author:
        - Shankar Kulumani 20 Nov 2017
            - only now realized I already implemented other orbit types
        - Shankar Kulumani 5 Dec 2016
            - Convert to python
        - Shankar Kulumani 15 Sept 2012
            - modified from USAFA code and notes from AAE532
            - only elliptical case will add other later
        - Shankar Kulumani 17 Sept 2012
            - added rev check to reduce angle btwn 0 and 2*pi

    References
        - AAE532 notes
        - Vallado 3rd Ed
    """
    small = 1e-9

    if ecc <= small:  # circular
        E = nu
        M = nu
    elif small < ecc and ecc <= 1 - small:  # elliptical
        sine = (np.sqrt(1.0 - ecc * ecc) * np.sin(nu)) / \
            (1.0 + ecc * np.cos(nu))
        cose = (ecc + np.cos(nu)) / (1.0 + ecc * np.cos(nu))

        E = np.arctan2(sine, cose)
        M = E - ecc * np.sin(E)

        E = attitude.normalize(E, 0, 2 * np.pi)
        M = attitude.normalize(M, 0, 2 * np.pi)

    elif np.absolute(ecc - 1) <= small:  # parabolic
        B = np.tan(nu / 2)

        E = B
        M = B + 1.0 / 3 * B**3
        # TODO: Need to check if I need to do quadrant checks for parabolic or hyperbolic cases
        # E = revcheck(E);
        # M = revcheck(M);
    elif ecc > 1 + small:  # hyperbolic
        sine = (np.sqrt(ecc**2 - 1) * np.sin(nu)) / \
            (1.0 + ecc * np.cos(nu))
        H = np.arcsinh(sine)
        E = H
        M = ecc * np.sinh(H) - H

        # E = revcheck(E);
        # M = revcheck(M);
    else:
        print("Eccentricity is out of bounds 0 < ecc < inf")

    return (E, M)

def kepler_eq_E(M_in, ecc_in):
    """Solve Kepler's Equation for all orbit types

    (E, nu, count) = kepler_eq_E(M, ecc)

    Purpose:
       - This function solves Kepler's equation for eccentric anomaly
       given a mean anomaly using a newton-rapson method.
           - Will work for elliptical/parabolic/hyperbolic orbits

    Inputs:
       - M - mean anomaly in rad -2*pi < M < 2*pi
       - ecc - eccentricity 0 < ecc < inf

    Outputs:
       - E - eccentric anomaly in rad 0 < E < 2*pi
       - nu - true anomaly in rad 0 < nu < 2*pi
       - count - number of iterations to converge

    Dependencies:
       - numpy - everything needs numpy
       - kinematics.attitude.normalize - normalize an angle

    Author:
       - Shankar Kulumani 15 Sept 2012
           - rewritten from code from USAFA
           - solve for elliptical orbits add others later
       - Shankar Kulumani 29 Sept 2012
           - added parabolic/hyperbolic functionality
       - Shankar Kulumani 7 Dec 2014
          - added loop for vector inputs
       - Shankar Kulumani 2 Dec 2016
          - converted to python and removed the vector inputs

    References
       - USAFA Astro 321 LSN 24-25
       - Vallado 3rd Ed pg 72
    """
    tol = 1e-9
    max_iter = 50

    E_out = []
    nu_out = []
    count_out = []

    if not hasattr(M_in, "__iter__"):
        M_in = [M_in]

    if not hasattr(ecc_in, "__iter__"):
        ecc_in = [ecc_in]

    for M, ecc in zip(M_in, ecc_in):
        # eccentricity check
        """
            HYPERBOLIC ORBIT
        """
        if ecc - 1.0 > tol:  # eccentricity logic
            # initial guess
            if ecc < 1.6:  # initial guess logic
                if M < 0.0 and (M > -np.pi or M > np.pi):
                    E_0 = M - ecc
                else:
                    E_0 = M + ecc

            else:
                if ecc < 3.6 and np.absolute(M) > np.pi:
                    E_0 = M - np.sign(M) * ecc
                else:
                    E_0 = M / (ecc - 1.0)

            # netwon's method iteration to find hyperbolic anomaly
            count = 1
            E_1 = E_0 + ((M - ecc * np.sinh(E_0) + E_0) /
                         (ecc * np.cosh(E_0) - 1.0))
            while ((np.absolute(E_1 - E_0) > tol) and (count <= max_iter)):
                E_0 = E_1
                E_1 = E_0 + ((M - ecc * np.sinh(E_0) + E_0) /
                             (ecc * np.cosh(E_0) - 1.0))
                count = count + 1

            E = E_0
            # find true anomaly
            sinv = -(np.sqrt(ecc * ecc - 1.0) * np.sinh(E_1)) / \
                (1.0 - ecc * np.cosh(E_1))
            cosv = (np.cosh(E_1) - ecc) / (1.0 - ecc * np.cosh(E_1))
            nu = np.arctan2(sinv, cosv)
        else:
            """
                PARABOLIC
            """
            if np.absolute(ecc - 1.0) < tol:  # parabolic logic
                count = 1

                S = 0.5 * (np.pi / 2 - np.arctan(1.5 * M))
                W = np.arctan(np.tan(S)**(1.0 / 3.0))

                E = 2.0 * 1.0 / np.tan(2.0 * W)

                nu = 2.0 * np.arctan(E)
            else:
                """
                    ELLIPTICAl
                """
                if ecc > tol:   # elliptical logic

                    # determine intial guess for iteration
                    if M > -np.pi and (M < 0 or M > np.pi):
                        E_0 = M - ecc
                    else:
                        E_0 = M + ecc

                    # newton's method iteration to find eccentric anomaly
                    count = 1
                    E_1 = E_0 + (M - E_0 + ecc * np.sin(E_0)) / \
                        (1.0 - ecc * np.cos(E_0))
                    while ((np.absolute(E_1 - E_0) > tol) and (count <= max_iter)):
                        count = count + 1
                        E_0 = E_1
                        E_1 = E_0 + (M - E_0 + ecc * np.sin(E_0)) / \
                            (1.0 - ecc * np.cos(E_0))

                    E = E_0

                    # find true anomaly
                    sinv = (np.sqrt(1.0 - ecc * ecc) * np.sin(E_1)) / \
                        (1.0 - ecc * np.cos(E_1))
                    cosv = (np.cos(E_1) - ecc) / (1.0 - ecc * np.cos(E_1))
                    nu = np.arctan2(sinv, cosv)
                else:
                    """
                        CIRCULAR
                    """
                    # -------------------- circular -------------------
                    count = 0
                    nu = M
                    E = M

        E_out.append(E)
        nu_out.append(attitude.normalize(nu, 0, 2 * np.pi))
        count_out.append(count)

    return (np.squeeze(E_out), np.squeeze(nu_out), np.squeeze(count_out))

def lvlh2pqw(r_lvlh, theta):
    r"""Convert a vector from LVLH to PQW reference frames

    This function will transform a vector represented in the local vertical/
    local horizontal reference frame to the perifocal reference frame.
    This transformation is equivalent to a rotation by the true anomaly about
    the angular moment vector.

    Parameters
    ----------
    r_lvlh : ndarray (3,)
        Vector defined in the LVLH frame (r_hat, thetahat, h_hat)
    theta : float 
        True anomaly defined in radians. Angle between the reference direction
        usually periapsis and the position vector in the plane of the orbit 
        and in the direction of motion

    Returns
    -------
    r_pqw : ndarray (3,)
        Vector represented in the perifocal frame (p_hat, q_hat, h_hat)
        same units as the input

    Author
    ------
    Shankar Kulumani		GWU		skulumani@gwu.edu

    References
    ----------
    Look at any astrodynamics book

    """
    R_lvlh2pqw = np.array([[ np.cos(theta), -np.sin(theta), 0],
                           [ np.sin(theta), np.cos(theta), 0],
                           [0             ,             0, 1]])
    r_pqw = R_lvlh2pqw.dot(r_lvlh)

    return r_pqw
