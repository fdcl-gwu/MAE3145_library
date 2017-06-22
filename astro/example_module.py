"""Module name

Extended description of the module

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
from __future__ import absolute_import, division, print_function, unicode_literals
# this allows for some compatibility between Python 2 and 3 but is not
# necessary

# import any other modules you need here
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# your personal modules should come after those included with Python

def add_two_inputs(a, b):
    r"""A one line description of the function

    This function will take two inputs and find the sum. 
    The inputs can be either scalars or numpy arrays of the same size.

    Parameters
    ----------
    a : any int or float  
        First input
    b : any int or float
        Another input

    Returns
    -------
    out : same as input
        Sum of a and b.

    Notes
    -----
    Both inputs should be the same size

    Author
    ------
    Shankar Kulumani		GWU		skulumani@gwu.edu

    Examples
    --------
    An example of how to use the function

    >>> a = [1, 2, 3]
    >>> b = [2, 3, 4]
    >>> out = add_two_inputs(a, b)
    out = [3, 5, 7]

    """
    out = a + b
    return out

