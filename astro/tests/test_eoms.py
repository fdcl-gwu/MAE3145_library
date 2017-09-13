from .. import eoms, constants
import numpy as np


def test_unity_gravity_force():
    m1 = 1
    m2 = 1
    r12 = np.array([1, 0, 0])
    F12 = eoms.gravity_force(m1, m2, r12)
    np.testing.assert_allclose(F12, -np.array([constants.G, 0, 0]))


class TesteomTBI():
    r10 = np.array([0, 0, 0])
    r20 = np.array([1, 0, 0])
    v10 = np.array([0, 0, 0])
    v20 = np.array([1, 1, 0])

    r0 = r20 - r10
    state = np.concatenate((r10, v10, r20, v20))
    t = 0
    m1 = 2
    m2 = 1
    G = 1
    statedot = eoms.eomTBI(state, t, m1, m2, G)

    def test_correct_size(self):
        np.testing.assert_allclose(self.statedot.shape, (12,))

    def test_known_statedot(self):
        """I can plug in these values and compute exactly what statedot should return

        This is exaclty copied from the homework assignment and lets me verify 
        my function automatically.
        """
        expected_statedot = np.concatenate((np.array([0, 0, 0]),
                                            np.array([1, 0, 0]),
                                            np.array([1, 1, 0]), 
                                            np.array([-2, 0, 0])))
        np.testing.assert_allclose(self.statedot, expected_statedot)
