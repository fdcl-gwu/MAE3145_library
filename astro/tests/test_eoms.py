from .. import eoms, constants
import numpy as np

def test_unity_gravity_force():
    m1 = 1
    m2 = 1
    r12 = np.array([1, 0 ,0])
    F12 = eoms.gravity_force(m1, m2, r12)
    np.testing.assert_allclose(F12, -np.array([constants.G, 0, 0]))

