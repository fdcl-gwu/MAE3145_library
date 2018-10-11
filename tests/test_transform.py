import numpy as np
from astro import transform

def test_that_everything_is_working():
    np.testing.assert_allclose(1, 1)

def test_all_angles_are_zero():
    raan = 0
    argp = 0 
    inc = 0
    PQW2ECI_expected = np.eye(3, 3)
    PQW2ECI = transform.pqw2eci(raan, argp, inc)

    np.testing.assert_allclose(PQW2ECI, PQW2ECI_expected)

def test_raan_ninety():
    raan = np.pi/2
    argp = 0
    inc = 0
    
    r_pqw = np.array([1, 0, 0])
    r_eci = np.array([0, 1, 0])
    
    np.testing.assert_array_almost_equal(transform.pqw2eci(raan, argp, inc).dot(r_pqw), r_eci)

def test_raan_oneeighty():
    raan = np.pi
    argp = 0
    inc = 0
    
    r_pqw = np.array([1, 0, 0])
    r_eci = np.array([-1, 0, 0])
    
    np.testing.assert_array_almost_equal(transform.pqw2eci(raan, argp, inc).dot(r_pqw), r_eci)
    
