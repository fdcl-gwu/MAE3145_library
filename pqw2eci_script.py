import numpy as np
from astro.transform import pqw2eci
# from kinematics.attitude import rot1, rot2, rot3


raan = np.deg2rad(45)
argp = np.deg2rad(195)
inc = 0

r_pqw = np.array([10000, 350, 4757])
r_eci = pqw2eci(raan, argp, inc).dot(r_pqw)
print(r_eci)
