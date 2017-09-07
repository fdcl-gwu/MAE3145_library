"""Testing module for example_module.py

This module will hold many tests to ensure that our code is actually doing what
it is supposed to do. Since testing is so critical we have a seperate place to
define these tests. In addition, we should continually test as we're always
going to be changing/improving our code. As a result, all of our testing should
be as automatic and simple as possible.

Author
------
Shankar Kulumani		GWU		skulumani@gwu.edu
"""

import numpy as np  # numpy will allow us to do the actual testing

# we import the module or functions we want to test
from astro import example_module


def test_add_two_inputs_scalar():
    """We define a test function to perform the tests.

    The documentation doesn't have to be as extensive, but the funciton name
    should be long and very descriptive.  There can be many tests and each test
    will only test a single function.  If you function has many branches, due
    to if statements or logic, then you will need a test to test each
    possibility of your code.
    """
    a = 2
    b = 3
    actual_out = example_module.add_two_inputs(a, b)
    expected_out = 5
    # this assertions tells Python that the output should match what we exepct.
    # If the test fails then we instantly know that something is wrong with our
    # code
    np.testing.assert_equal(actual_out, expected_out)


def test_add_two_inputs_numpy_arrays():
    """This function will test two array inputs

    We can possibly input arrays into our function so we should make sure that
    works as well.
    """

    a = np.array([1, 23, 5])
    b = np.array([2, 5, 1])
    expected_out = np.array([3, 28, 6])
    actual_out = example_module.add_two_inputs(a, b)
    # there are many kinds of assertions built into Numpy. They allow
    # comparisions between scalars, arrays, strings, and at various tolerances
    # for the case of floats.
    np.testing.assert_allclose(actual_out, expected_out)


def test_add_two_inputs_large_random_arrays():
    """Our function should hopefully be able to handle any sized array

    """
    a = np.random.rand(1000000)
    b = np.random.rand(1000000)
    expected_out = a + b
    actual_out = example_module.add_two_inputs(a, b)
    np.testing.assert_allclose(actual_out, expected_out)


def test_always_pass():
    """Here's a test that will always pass
    """
    np.testing.assert_allclose(1, 1)
