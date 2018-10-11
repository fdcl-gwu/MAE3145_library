"""Example converting RV to classical orbital elements

"""

import numpy as np
from astro import constants, kepler
import matplotlib.pyplot as plt

    # plot the orbit in the perifocal reference frame
    # true_anomaly = np.linspace(0, 2 * np.pi, 1000)
    # radius = p / (1 + ecc * np.cos(true_anomaly))

    # fig, ax = plt.subplots()
    # ax.plot(radius * np.cos(true_anomaly), radius * np.sin(true_anomaly))
    # ax.plot(np.linalg.norm(r) * np.cos(nu * np.pi/180), np.linalg.norm(r) * np.sin(nu * np.pi/180), 'bo', markersize=10)
    # ax.plot(0, 0, 'bo', markersize=20)
    # ax.set_xlabel('$\hat p$')
    # ax.set_ylabel('$\hat q$')
    # plt.grid()
    # plt.show()
    
def example_one():
    re = constants.earth.radius
    r = np.array([1.6772 * re, -1.6772 * re, 2.3719 * re])  # position in ECI in kilometers
    v = np.array([3.1544, 2.4987, 0.4658])  # velocity in ECI in km/sec

    a, ecc, inc, raan, argp, nu = kepler.rv2coe(r, v)

def example_two():
    r = np.array([6524.834, 6862.875, 6448.296])  # position in ECI in kilometers
    v = np.array([4.901327, 5.53376, -1.976341])  # velocity in ECI in km/sec

    kepler.rv2coe(r, v)

if __name__ == '__main__':
    example_one()
    example_two()

