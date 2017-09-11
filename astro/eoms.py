# Compute gravity

"""Bigger comment

More comments


"""

import numpy as np

def gravity_force(m1, m2, G, r12_vector):
    mag = np.linalg.norm(r12_vector)

    unit_vector = r12_vector / mag

    F12 = - (G * m1 * m2 / mag**2 ) * unit_vector

    return F12
