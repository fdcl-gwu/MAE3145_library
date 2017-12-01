"""test all the functions in planets 
"""
import numpy as np

from astro import planets, time
import pdb


rtol = 1e-0

def test_sun_earth_eci_usafa():
    jd = 2453905.50000000
    expected_rsun = [6371243.918400, 139340081.269385, 60407749.811252]
    rsun, ra, dec = planets.sun_earth_eci(jd)
    np.testing.assert_allclose(rsun, expected_rsun, rtol=1e-4)

def test_sun_eci_vallado():
    jd, mjd = time.date2jd(1994, 4, 2, 0, 0, 0)
    jd_vallado = 2449444.5
    rsun_vallado = np.array([146241097,
                             28574940,
                             12389196])
    ra_vallado, dec_vallado = np.deg2rad(11.056071), np.deg2rad(4.7529393)
    rsun, ra, dec = planets.sun_earth_eci(jd)


    np.testing.assert_allclose(jd, jd_vallado)
    np.testing.assert_allclose(rsun, rsun_vallado, rtol=1e-4)
    np.testing.assert_allclose((ra, dec), (ra_vallado, dec_vallado), rtol=1e-4)


