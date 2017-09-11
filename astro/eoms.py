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

    F12 = - (G * m1 * m2 / mag**2 ) * unit_vector

    return F12
