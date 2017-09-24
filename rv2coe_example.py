"""Example converting RV to classical orbital elements

"""

import numpy as np
from astro import constants

re = constants.earth.radius
mu = constants.earth.mu

r = np.array([1.6772 * re, -1.6772 * re, 2.3719 * re])  # position in ECI in kilometers
v = np.array([3.1544, 2.4987, 0.4658])  # velocity in ECI in km/sec
