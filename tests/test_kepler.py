"""Test out our kepler module
"""

import numpy as np
from astro import kepler, constants

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

class Testrv2coeEquatorialCircular():

    p_true = 6378.137 # km
    ecc_true = 0.0
    inc_true = 0.0
    raan_true = 0.0
    arg_p_true = 0.0
    nu_true = 0.0
    mu = 398600.5 # km^3 /sec^2

    R_ijk_true = np.array([6378.137,0,0])
    V_ijk_true = np.sqrt(mu/p_true) * np.array([0,1,0])
    
    p, a, ecc, inc, raan, arg_p, nu, m, arglat, truelon, lonper = kepler.rv2coe(R_ijk_true, V_ijk_true, mu)
    
    def test_p(self):
        np.testing.assert_allclose(self.p, self.p_true)
    
    def test_a(self):
        np.testing.assert_allclose(self.a, self.p_true / (1 - self.ecc_true**2))

    def test_ecc(self):
        np.testing.assert_allclose(self.ecc, self.ecc_true)
    
    def test_inc(self):
        np.testing.assert_allclose(self.inc, self.inc_true)

    def test_raan(self):
        np.testing.assert_allclose(self.raan, self.raan_true)

    def test_arg_p(self):
        np.testing.assert_allclose(self.arg_p, self.arg_p_true)
    
    def test_nu(self):
        np.testing.assert_allclose(self.nu, self.nu_true)

    def test_m(self):
        E_true, M_true = kepler.nu2anom(self.nu, self.ecc)
        np.testing.assert_allclose(self.m, M_true)

    def test_arglat(self):
        np.testing.assert_allclose(self.arglat, self.nu_true + self.arg_p_true)

    def test_truelon(self):
        np.testing.assert_allclose(self.truelon, self.nu_true + self.raan_true + self.arg_p_true)

    def test_lonper(self):
        np.testing.assert_allclose(self.lonper, self.arg_p_true + self.raan_true)



class Testrv2coePolarCircular():

    p_true = 6378.137 # km
    ecc_true = 0.0
    inc_true = np.pi / 2
    raan_true = 0.0
    arg_p_true = 0.0
    nu_true = 0.0
    mu = 398600.5 # km^3 /sec^2

    R_ijk_true = np.array([6378.137,0,0])
    V_ijk_true = np.sqrt(mu/p_true) * np.array([0,0,1])
    
    p, a, ecc, inc, raan, arg_p, nu, m, arglat, truelon, lonper = kepler.rv2coe(R_ijk_true, V_ijk_true, mu)
    
    def test_p(self):
        np.testing.assert_allclose(self.p, self.p_true)
    
    def test_a(self):
        np.testing.assert_allclose(self.a, self.p_true / (1 - self.ecc_true**2))

    def test_ecc(self):
        np.testing.assert_allclose(self.ecc, self.ecc_true)
    
    def test_inc(self):
        np.testing.assert_allclose(self.inc, self.inc_true)

    def test_raan(self):
        np.testing.assert_allclose(self.raan, self.raan_true)

    def test_arg_p(self):
        np.testing.assert_allclose(self.arg_p, self.arg_p_true)
    
    def test_nu(self):
        np.testing.assert_allclose(self.nu, self.nu_true)

    def test_m(self):
        E_true, M_true = kepler.nu2anom(self.nu, self.ecc)
        np.testing.assert_allclose(self.m, M_true)

    def test_arglat(self):
        np.testing.assert_allclose(self.arglat, self.nu_true + self.arg_p_true)

    def test_truelon(self):
        np.testing.assert_allclose(self.truelon, self.nu_true + self.raan_true + self.arg_p_true)

    def test_lonper(self):
        np.testing.assert_allclose(self.lonper, self.arg_p_true + self.raan_true)

class Testrv2coeEquatorialCircularQuarer():

    p_true = 6378.137 # km
    ecc_true = 0.0
    inc_true = 0.0
    raan_true = 0.0
    arg_p_true = 0.0
    nu_true = np.pi /2
    mu = 398600.5 # km^3 /sec^2

    R_ijk_true = np.array([0.0, 6378.137,0])
    V_ijk_true = np.sqrt(mu/p_true) * np.array([-1,0,0])
    
    p, a, ecc, inc, raan, arg_p, nu, m, arglat, truelon, lonper = kepler.rv2coe(R_ijk_true, V_ijk_true, mu)
    
    def test_p(self):
        np.testing.assert_allclose(self.p, self.p_true)
    
    def test_a(self):
        np.testing.assert_allclose(self.a, self.p_true / (1 - self.ecc_true**2))

    def test_ecc(self):
        np.testing.assert_allclose(self.ecc, self.ecc_true)
    
    def test_inc(self):
        np.testing.assert_allclose(self.inc, self.inc_true)

    def test_raan(self):
        np.testing.assert_allclose(self.raan, self.raan_true)

    def test_arg_p(self):
        np.testing.assert_allclose(self.arg_p, self.arg_p_true)
    
    def test_nu(self):
        np.testing.assert_allclose(self.nu, self.nu_true)

    def test_m(self):
        E_true, M_true = kepler.nu2anom(self.nu, self.ecc)
        np.testing.assert_allclose(self.m, M_true)

    def test_arglat(self):
        # argument of latitude isn't used for this case so it goes to zero
        # np.testing.assert_allclose(self.arglat, self.nu_true + self.arg_p_true)
        pass

    def test_truelon(self):
        np.testing.assert_allclose(self.truelon, self.nu_true + self.raan_true + self.arg_p_true)

    def test_lonper(self):
        np.testing.assert_allclose(self.lonper, self.arg_p_true + self.raan_true)

class Testrv2coeVallado():

    p_true = 1.73527 * constants.earth.radius # km
    ecc_true = 0.83285
    inc_true = np.deg2rad(87.87)
    raan_true = np.deg2rad(227.89)
    arg_p_true = np.deg2rad(53.38)
    nu_true = np.deg2rad(92.335)
    mu = 398600.5 # km^3 /sec^2

    R_ijk_true = np.array([6524.834, 6862.875, 6448.296])
    V_ijk_true = np.array([4.901320, 5.533756, -1.976341]) 
    
    p, a, ecc, inc, raan, arg_p, nu, m, _, _, _= kepler.rv2coe(R_ijk_true, V_ijk_true, mu)
    
    rtol = 1e-3

    def test_p(self):
        np.testing.assert_allclose(self.p, self.p_true, rtol=self.rtol)
    
    def test_a(self):
        np.testing.assert_allclose(self.a, self.p_true / (1 - self.ecc_true**2), rtol=self.rtol)

    def test_ecc(self):
        np.testing.assert_allclose(self.ecc, self.ecc_true, rtol=self.rtol)
    
    def test_inc(self):
        np.testing.assert_allclose(self.inc, self.inc_true, rtol=self.rtol)

    def test_raan(self):
        np.testing.assert_allclose(self.raan, self.raan_true, rtol=self.rtol)

    def test_arg_p(self):
        np.testing.assert_allclose(self.arg_p, self.arg_p_true, rtol=self.rtol)
    
    def test_nu(self):
        np.testing.assert_allclose(self.nu, self.nu_true, rtol=self.rtol)

    def test_m(self):
        E_true, M_true = kepler.nu2anom(self.nu, self.ecc)
        np.testing.assert_allclose(self.m, M_true, rtol=self.rtol)


class Testrv2coeCurtis():
    """Using example 4.7 from Curtis
    """
    p_true = 80000**2/398600
    ecc_true = 1.4
    inc_true = np.deg2rad(30)
    raan_true = np.deg2rad(40)
    arg_p_true = np.deg2rad(60)
    nu_true = np.deg2rad(30)
    mu = 398600 # km^3 /sec^2

    R_ijk_true = np.array([-4040, 4815, 3629])
    V_ijk_true = np.array([-10.39, -4.772, 1.744]) 
    
    p, a, ecc, inc, raan, arg_p, nu, m, _, _, _= kepler.rv2coe(R_ijk_true, V_ijk_true, mu)
    
    rtol = 1e-3

    def test_p(self):
        np.testing.assert_allclose(self.p, self.p_true, rtol=self.rtol)
    
    def test_a(self):
        np.testing.assert_allclose(np.absolute(self.a), self.p_true / (self.ecc_true**2 - 1), rtol=1e2)

    def test_ecc(self):
        np.testing.assert_allclose(self.ecc, self.ecc_true, rtol=1e-1)
    
    def test_inc(self):
        np.testing.assert_allclose(self.inc, self.inc_true, rtol=self.rtol)

    def test_raan(self):
        np.testing.assert_allclose(self.raan, self.raan_true, rtol=self.rtol)

    def test_arg_p(self):
        np.testing.assert_allclose(self.arg_p, self.arg_p_true, rtol=self.rtol)
    
    def test_nu(self):
        np.testing.assert_allclose(self.nu, self.nu_true, rtol=self.rtol)

    def test_m(self):
        E_true, M_true = kepler.nu2anom(self.nu, self.ecc)
        np.testing.assert_allclose(self.m, M_true, rtol=self.rtol)


class Testrv2coeRV1():
    a_true = 8697.5027
    ecc_true = 0.2802
    p_true = a_true * ( 1 - ecc_true**2)
    inc_true = np.deg2rad(33.9987)
    raan_true = np.deg2rad(250.0287)
    arg_p_true = np.deg2rad(255.5372)
    nu_true = np.deg2rad(214.8548)
    mu = 398600.5

    r = np.array([8840, 646, 5455])
    v = np.array([-0.6950, 5.250, -1.65])

    p, a, ecc, inc, raan, arg_p, nu, m, arglat, truelon, lonper = kepler.rv2coe(r, v, mu)

    def test_p(self):
        np.testing.assert_allclose(self.p, self.p_true, rtol=1e-1)
    
    def test_a(self):
        np.testing.assert_allclose(self.a, self.p_true / (1 - self.ecc_true**2))

    def test_ecc(self):
        np.testing.assert_allclose(self.ecc, self.ecc_true, rtol=1e-4)
    
    def test_inc(self):
        np.testing.assert_allclose(self.inc, self.inc_true, rtol=1e-4)

    def test_raan(self):
        np.testing.assert_allclose(self.raan, self.raan_true)

    def test_arg_p(self):
        np.testing.assert_allclose(self.arg_p, self.arg_p_true, rtol=1e-4)
    
    def test_nu(self):
        np.testing.assert_allclose(self.nu, self.nu_true, rtol=1e-4)

    def test_m(self):
        E_true, M_true = kepler.nu2anom(self.nu, self.ecc)
        np.testing.assert_allclose(self.m, M_true)

    def test_arglat(self):
        # argument of latitude isn't used for this case so it goes to zero
        # np.testing.assert_allclose(self.arglat, self.nu_true + self.arg_p_true)
        pass

    def test_truelon(self):
        # not used for inclined orbits - only special ones
        # np.testing.assert_allclose(self.truelon, self.nu_true + self.raan_true + self.arg_p_true)
        pass

    def test_lonper(self):
        # not really used for inclined orbits
        # np.testing.assert_allclose(self.lonper, self.arg_p_true + self.raan_true)
        pass

class Testrv2coeEquatorialCircularHalf():

    p_true = 6378.137 # km
    ecc_true = 0.0
    inc_true = 0.0
    raan_true = 0.0
    arg_p_true = 0.0
    nu_true = np.pi
    mu = 398600.5 # km^3 /sec^2

    R_ijk_true = np.array([-p_true, 0,0])
    V_ijk_true = np.sqrt(mu/p_true) * np.array([0,-1,0])
    
    p, a, ecc, inc, raan, arg_p, nu, m, arglat, truelon, lonper = kepler.rv2coe(R_ijk_true, V_ijk_true, mu)
    
    def test_p(self):
        np.testing.assert_allclose(self.p, self.p_true)
    
    def test_a(self):
        np.testing.assert_allclose(self.a, self.p_true / (1 - self.ecc_true**2))

    def test_ecc(self):
        np.testing.assert_allclose(self.ecc, self.ecc_true)
    
    def test_inc(self):
        np.testing.assert_allclose(self.inc, self.inc_true)

    def test_raan(self):
        np.testing.assert_allclose(self.raan, self.raan_true)

    def test_arg_p(self):
        np.testing.assert_allclose(self.arg_p, self.arg_p_true)
    
    def test_nu(self):
        np.testing.assert_allclose(self.nu, self.nu_true)

    def test_m(self):
        E_true, M_true = kepler.nu2anom(self.nu, self.ecc)
        np.testing.assert_allclose(self.m, M_true)

    def test_arglat(self):
        # argument of latitude isn't used for this case so it goes to zero
        # np.testing.assert_allclose(self.arglat, self.nu_true + self.arg_p_true)
        pass

    def test_truelon(self):
        np.testing.assert_allclose(self.truelon, self.nu_true + self.raan_true + self.arg_p_true)

    def test_lonper(self):
        np.testing.assert_allclose(self.lonper, self.arg_p_true + self.raan_true)


def test_nu2anom():
    """
        A matlab test case which is copied here
    """
    M_matlab = np.deg2rad(110)
    ecc = 0.9
    E_matlab = 2.475786297687611 
    nu_matlab = 2.983273149717047

    E_python, M_python = kepler.nu2anom(nu_matlab,ecc)

    np.testing.assert_allclose(E_python, E_matlab)
    np.testing.assert_allclose(M_python, M_matlab)

def test_nu2anom_zero():
    """
        Make sure that at zero nu=E=M
    """
    M_true = 0.0
    ecc = 1.2
    E_true = 0.0
    nu_true = 0.0

    E_python, M_python = kepler.nu2anom(nu_true,ecc)

    np.testing.assert_allclose((E_python, M_python),(E_true,M_true))


def test_nu2anom_pi():
    """
        Make sure that at pi nu=E=M
    """
    M_true = np.pi
    ecc = 0.9
    E_true = np.pi
    nu_true = np.pi
    
    E_python, M_python = kepler.nu2anom(nu_true,ecc)

    np.testing.assert_allclose(E_python, E_true)
    np.testing.assert_allclose(M_python, M_true)
