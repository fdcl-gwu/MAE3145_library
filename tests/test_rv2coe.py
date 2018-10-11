import numpy as np
from astro import kepler

def test_rv2coe_project_example_one():
    r = np.array([8840, 646, 5455])
    v = np.array([-0.695, 5.25, -1.65])

    a, ecc, inc, raan, argp, nu = kepler.rv2coe(r, v)
    
    # expected values
    a_exp = 8697.5027
    ecc_exp = 0.2802

    np.testing.assert_allclose(a, a_exp)
    np.testing.assert_allclose(ecc, ecc_exp, rtol=1e-4)
