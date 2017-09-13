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


def eomTBI(state, t, m1, m2, G):
    r"""This simulates the motion of two bodies under their mutual
        gravity.

    Extended description of the function.

    Parameters
    ----------
    var1 : array_like and type
        <`4:Description of the variable`>

    Returns
    -------
    describe : type
        Explanation of return value named describe

    Other Parameters
    ----------------
    only_seldom_used_keywords : type
        Explanation of this parameter

    Raises
    ------
    BadException
        Because you shouldn't have done that.

    See Also
    --------
    other_func: Other function that this one might call

    Notes
    -----
    You may include some math:

    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

    Author
    ------
    Shankar Kulumani		GWU		skulumani@gwu.edu

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] Shannon, Claude E. "Communication theory of secrecy systems."
    Bell Labs Technical Journal 28.4 (1949): 656-715

    Examples
    --------
    An example of how to use the function

    >>> a = [1, 2, 3]
    >>> print [x + 3 for x in a]
    [4, 5, 6]
    >>> print "a\n\nb"
    a
    b

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
    
    statedot = np.concatenate(( r1_dot, v1_dot, r2_dot, v2_dot ))

    return statedot
