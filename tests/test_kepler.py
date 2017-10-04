
import numpy as np
from astro import kepler

def test_specific_mechanicl_energy_zero_velocity():
    v = 0
    r = 1
    mu = 5
    expected_energy = - mu

    actual_energy = kepler.specific_mechanical_energy(r, v, mu)

    np.testing.assert_allclose(actual_energy, expected_energy)

def test_specific_mechanicl_energy_ones():
    v = 1
    r = 1
    mu = 10
    expected_energy = 1/2 - mu
    actual_energy = kepler.specific_mechanical_energy(r, v, mu)
    np.testing.assert_allclose(actual_energy, expected_energy)

def test_apoapsis_periapsis_circular():
    a = 6378
    ecc = 0
    expected_rp = a
    expected_ra = a

    actual_ra, actual_rp = kepler.apoapsis_periapsis(a, ecc)

    np.testing.assert_allclose(actual_ra, expected_ra)
    np.testing.assert_allclose(actual_rp, expected_rp)
