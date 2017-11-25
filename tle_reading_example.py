"""Example for reading and using the TLE module
"""
from __future__ import absolute_import, division, print_function, unicode_literals

from astro import tle, time
import numpy as np

filename = './data/example_tle.txt'

tles = tle.get_tle(filename)

# iterate over the tles list
for tle in tles:
    print('---------------------TLE Data from {}--------------------------'.format(tle.satname))
    yr = 2000+ tle.epoch_year
    mo, day, hr, mn, sec = time.dayofyr2mdhms(yr, tle.epoch_day)
    print('Epoch : {} JD'.format(time.date2jd(yr, mo, day, hr, mn, sec)[0]))

