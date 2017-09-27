"""Example converting RV to classical orbital elements

"""

import numpy as np
from astro import constants
import matplotlib.pyplot as plt

re = constants.earth.radius
mu = constants.earth.mu

def rv2coe(r, v):
    """THIS FUNCTION STILL NEEDS TO CHECK THE QUADRANTS FOR ALL ANGLES

    """

    print("YOU NEED TO MANUALLY VERIFY THE ANGLES!!!")

    h = np.cross(r, v)
    h_hat = h / np.linalg.norm(h)
    print('h_hat: {}'.format(h_hat))

    n = np.cross(np.array([0, 0, 1]), h_hat)
    n_hat = n / np.linalg.norm(n)
    print('n_hat: {}'.format(n_hat))

    e = 1 / mu * (( np.linalg.norm(v)**2 - mu / np.linalg.norm(r)) * r - r.dot(v) * v)
    e_hat = e / np.linalg.norm(e)
    print('e_hat: {}'.format(e_hat))

    p = np.linalg.norm(h)**2 / mu
    ecc = np.linalg.norm(e)
    a = p / (1-ecc**2)
    print('p: {} km, a: {} km, ecc: {}'.format(p, a, ecc))
    print('p: {} Re, a: {} Re'.format(p / re, a / re))

    inc = np.arccos(np.dot(np.array([0, 0, 1]), h_hat)) * 180 / np.pi
    print('i: {} deg'.format(inc))

    raan = np.arccos(np.dot(np.array([1, 0, 0]), n_hat)) * 180 / np.pi
    print('raan: {} deg'.format(raan))

    argp = np.arccos(np.dot(n_hat, e_hat)) * 180 / np.pi
    print('argp: {} deg'.format(argp))

    nu = np.arccos(np.dot(e_hat, r / np.linalg.norm(r))) * 180 / np.pi
    print('nu: {} deg'.format(nu))

    # plot the orbit in the perifocal reference frame
    true_anomaly = np.linspace(0, 2 * np.pi, 1000)
    radius = p / (1 + ecc * np.cos(true_anomaly))

    fig, ax = plt.subplots()
    ax.plot(radius * np.cos(true_anomaly), radius * np.sin(true_anomaly))
    ax.plot(np.linalg.norm(r) * np.cos(nu * np.pi/180), np.linalg.norm(r) * np.sin(nu * np.pi/180), 'bo', markersize=10)
    ax.plot(0, 0, 'bo', markersize=20)
    ax.set_xlabel('$\hat p$')
    ax.set_ylabel('$\hat q$')
    plt.grid()
    plt.show()

def example_one():
    r = np.array([1.6772 * re, -1.6772 * re, 2.3719 * re])  # position in ECI in kilometers
    v = np.array([3.1544, 2.4987, 0.4658])  # velocity in ECI in km/sec

    rv2coe(r, v)

def example_two():
    r = np.array([6524.834, 6862.875, 6448.296])  # position in ECI in kilometers
    v = np.array([4.901327, 5.53376, -1.976341])  # velocity in ECI in km/sec

    rv2coe(r, v)

if __name__ == '__main__':
    example_one()
    example_two()

