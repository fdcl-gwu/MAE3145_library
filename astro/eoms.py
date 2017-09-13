"""Functions for equations of motion in astrodynamics

Some examples from class

Notes
-----
    This is an example of an indented section. It's like any other section,
    but the body is indented to help it stand out from surrounding text.

If a section is indented, then a section break is created by
resuming unindented text.

Attributes
----------
module_level_variable1 : int
    Descrption of the variable

Author
------
Shankar Kulumani		GWU		skulumani@gwu.edu
"""
import numpy as np
from astro import constants


def gravity_force(m1, m2, r12_vector, G=constants.G):
    r"""Compute the gravity between two masses

    Use newton's law of gravity to compute the magnitude and direction of
    the force due to gravity.
    This will output the force vector on m2 due to the gravity of m1.

    Parameters
    ----------
    m1 : float
        Mass of m1 in kilogram
    m2 : float
        Mass of m2 in kilogram
    G : float
        Newton's universal gravitational constant km^3/kg*sec^2
    r12_vector : (3,) numpy array
        Vector from m1 to m2 in units of kilometer

    Returns
    -------
    <`5:F12`> : (3,) numpy array
        Force of m1 on m2. This will be in the opposite direction of the vector
        r12. Force is attractive and should point from m2 to m1

    See Also
    --------
    constants : Uses the gravitational constant from this function

    Notes
    -----
    You may include some math:

    .. math:: F_{12} = -G \frac{m_1 m_2}{r_{12}^3} r_{12}

    Author
    ------
    Shankar Kulumani		GWU		skulumani@gwu.edu

    References
    ----------

    .. [1] BATE, Roger R, MUELLER, Donald D y WHITE, Jerry E. Fundamentals of
    Astrodynamics. Courier Dover Publications, 1971. 

    Examples
    --------
    An example of how to use the function

    >>> r12 = np.array([1, 0, 0])
    >>> m1, m2 = (1, 1)
    >>> astro.eoms.gravity_force(m1, m2, r12)
    array([-6.67300000e-20, -0.0e0, -0.0e0])

    """
    mag = np.linalg.norm(r12_vector)

    unit_vector = r12_vector / mag

    F12 = - (G * m1 * m2 / mag**2) * unit_vector

    return F12


def eomTBI(state, t, m1, m2, G):
    r"""This simulates the motion of two bodies under their mutual
        gravity.

    This function is to be used with scipy.integrate.odeint and describes the 
    equations of motion of two point masses under the influence of their mutual
    gravitational attraction. 

    The dynamics are described with respect to an inertial reference frame.

    You can look at HW1 from MAE3145 for more details.

    Parameters
    ----------
    state : (12,) numpy array 
        state[0:3] - r1 position of m_1 wrt inertial frame in (dist) 
        state[3:6] - v1 velocity of m_1 wrt inertial frame (dist/time)
        state[6:9] - r2 position of m_2 wrt inertial frame (dist)
        state[9:12] - v2 velocity of m_2 wrt inertial frame in (dist/time)
    t : float
        Current simulation time (time)
    m1 : float
        Mass of m_1 (mass)
    m2 : float
        Mass of m_2 (mass)
    G : float
        Gravitational constant (dist^3/mass / time^2)

    Returns
    -------
    statedot : (12,) numpy array
        statedot[0:3] - r1_dot derivative of r1 wrt inertial frame (dist/time)
        statedot[3:6] - v1_dot derivative of v1 wrt inertial frame (dist/time^2)
        statedot[6:9] - r2_dot derivative of r2 wrt inertial frame (dist/time)
        statedot[9:12] - v2_dot derivative of v2 wrt inertial frame (dist/time^2)

    See Also
    --------
    gravity_force : Compute the gravitional FORCE between two masses (we need 
                    acceleration in this function so don't mess up the difference,
                    like I did in class)

    Notes
    -----
    You may include some math:

    .. math:: m_1 \ddot{r}_1 = G \frac{m_1 m_2}{\| r_2 - r_1\|^3} (r_2 - r_1)

    .. math:: m_2 \ddot{r}_2 = - G \frac{m_1 m_2}{\| r_2 - r_1\|^3} (r_2 - r_1)

    Author
    ------
    Shankar Kulumani		GWU		skulumani@gwu.edu

    References
    ----------

    .. [1] BATE, Roger R, MUELLER, Donald D y WHITE, Jerry E. Fundamentals of
    Astrodynamics. Courier Dover Publications, 1971. 
    .. [2] CURTIS, Howard D. Orbital mechanics for engineering students.
    Butterworth-Heinemann, 2013. 

    Examples
    --------

    python simTBI.py

    """

    r1 = state[0:3]
    v1 = state[3:6]
    r2 = state[6:9]
    v2 = state[9:12]

    r = r2 - r1
    r1_dot = v1
    v1_dot = gravity_force(m1, m2, -r, G) / m1
    r2_dot = v2
    v2_dot = gravity_force(m1, m2, r, G) / m2

    statedot = np.concatenate((r1_dot, v1_dot, r2_dot, v2_dot))

    return statedot
