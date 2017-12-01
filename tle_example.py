"""Example script which reads TLEs from a given file and prints out some data

"""

from astro import tle

# input file with all of the TLE data
filename = './data/example_tle.txt'

# if there are multiple TLEs, each TLE object is stored in a Python List
sats = tle.get_tle(filename)

# since it's a list we can iterate through the list and output some of the data
for sat in sats:
    print('\nsatname : {}, satnum : {}'.format(sat.satname, sat.satnum))

    print('\nYear is two digits, and a day with fraction. There is a function already to change this.')
    print('epoch_year : {}, epoch_day : {}'.format(sat.epoch_year, sat.epoch_day))

    print('\nNow print out some of the orbital elements')
    print('\nThese units are in rev/day. You will need to convert!')
    print('ndot_over_2 : {}, nddot_over_6 : {}'.format(sat.ndot_over_2, sat.nddot_over_6))

    print('\nMake sure you check the units! Degrees!')
    print('inc : {}, raan : {}, ecc : {}'.format(sat.inc, sat.raan, sat.ecc))
    print('M : {}, n : {}'.format(sat.ma, sat.mean_motion))
    


