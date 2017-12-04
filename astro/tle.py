
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
from collections import namedtuple

# tuple to hold all the items from a single TLE
TLE = namedtuple('TLE', [
    'satname', 'satnum', 'classification', 'id_year', 'id_launch',
    'id_piece', 'epoch_year', 'epoch_day', 'ndot_over_2', 'nddot_over_6',
    'bstar', 'ephtype', 'elnum', 'checksum1',
    'inc', 'raan', 'ecc', 'argp', 'ma', 'mean_motion', 'epoch_rev',
    'checksum2', 'good'])

def parsetle(l0, l1, l2):
    """Parses the three lines of a TLE to their appropriate values.

    Inputs
    ------
        l0 - first line consiting of the name of TLE 
        l1 - second line
        l2 - third line

    Outputs
    -------
    namedtuple TLE: A tuple holding all of the values associated with the TLE
        satname - satellite name
        satnum - satellite number found (0 if the requested sat was not found)
        classfication  - classification (classified, unclassified)
        id_year - launch year (last 2 digits)
        id_launch - launch number of the year
        id_piece - piece of launch (a string 3 characters long)
        epoch_year - epoch year (last 2 digits)
        epoch_day - epoch day of year
        ndot_over_2 - first time derive of mean mot. divided by 2 (rev/day^2)
        nddot_over_6 - 2nd deriv of mean mot div by 6 (rev/day^3)
        bstar - bstar drag term
        ephtype- ephemeris type
        elnum  - element number (modulo 1000)
        checksum1 - checksum of first line

        inc    - inclination (deg)
        raan   - right ascension of asc. node (deg)
        ecc    - eccentricity
        argp    - argument of perigee (deg)
        ma     - mean anomaly (deg)
        mean_motion - mean motion (revs per day)
        epoch_rev - revolution number(modulo 100,000)
        checksum2 - checksum of second line

    References
    ----------
    "Fundamental of Astrodynamics and Applictions, 2nd Ed", by Vallado
    www.celestrak.com/NORAD/documentation/tle-fmt.asp
    manpages.debian.net/cgi-bin/...
    display_man.cgi?id=e2095ebad4eb81b943fcdd55ec9b7521&format=html
    """
    try:
        # parse line zero
        satname = l0[0:23]

        # parse line one
        satnum = int(l1[2:7])
        classification = l1[7:8]
        id_year = int(l1[9:11])
        id_launch = int(l1[11:14])
        id_piece = l1[14:17]
        epoch_year = int(l1[18:20])
        epoch_day = float(l1[20:32])
        ndot_over_2 = float(l1[33:43])
        nddot_over_6 = stringScientificNotationToFloat(l1[44:52])
        bstar = stringScientificNotationToFloat(l1[53:61])
        ephtype = int(l1[62:63])
        elnum = int(l1[64:68])
        checksum1 = int(l1[68:69])

        # parse line 2
        # satellite        = int(line2[2:7])
        inc = float(l2[8:16])
        raan = float(l2[17:25])
        ecc = float(l2[26:33]) * 0.0000001
        argp = float(l2[34:42])
        ma = float(l2[43:51])
        mean_motion = float(l2[52:63])
        epoch_rev = float(l2[63:68])
        checksum2 = float(l2[68:69])

        good = True
    except: # We have a bad TLE but we're not sure where
        # parse line zero
        satname = l0[0:23]

        # parse line one
        satnum = 0
        classification = 'U'
        id_year = 0
        id_launch = 0
        id_piece = 'A'
        epoch_year = 0 
        epoch_day = 0
        ndot_over_2 = 0
        nddot_over_6 = 0
        bstar = 0
        ephtype = 0
        elnum = 0
        checksum1 = 0

        # parse line 2
        # satellite        = int(line2[2:7])
        inc = 0
        raan = 0
        ecc = 0
        argp = 0
        ma = 0
        mean_motion = 0
        epoch_rev = 0
        checksum2 = 0

        good = False

    return TLE(satnum=satnum, classification=classification, id_year=id_year,
               id_launch=id_launch, id_piece=id_piece, epoch_year=epoch_year,
               epoch_day=epoch_day, ndot_over_2=ndot_over_2,
               nddot_over_6=nddot_over_6, bstar=bstar, ephtype=ephtype,
               elnum=elnum, checksum1=checksum1, inc=inc, raan=raan, ecc=ecc,
               argp=argp, ma=ma, mean_motion=mean_motion, epoch_rev=epoch_rev,
               checksum2=checksum2, satname=satname, good=good)

def validtle(l0, l1, l2):
    r"""Ensure 3 line TLEs are valid.

    This function will check each line of a 3 line TLE and ensure they are
    valid. It assumes the format is that which is found on space-track.org.

    Parameters
    ----------
    l0 : string
        First line of TLE. This line holds the object name.
        Sometimes is starts with a 0 and other times it does not.
        Both will be valid in this code.
    l1: string
        Second line of TLE. This is first real line with real data.
        Should begin with a 1 and pass a checksum. There is also a line length
        requirement.
    l2: string
        Third line of TLE. This also contains data. Begins with a 2 and has a
        checksum and line lenght requirement.

    Returns
    -------
    boolean:
        This returns a boolean object which is the concatenation of all the
        requirements for the checking.  If this output is True then the three
        lines of the inputted TLE are probably valid.

    See Also
    --------
    checksum: another related function to calculate the line checksum
    parsetle: this will take the three lines and extract out the TLE data
    stringScientificNotationToFloat: Converts the TLE number format to float

    Notes
    -----
    TLEs are an old format, but they are well documented. In addition, the TLE
    has some inherent limitations on the expected accuracy of the ephemerides
    and the data contained within it.
    
    Author
    ------
    Shankar Kulumani 

    References
    ----------

    .. [1] VALLADO, David A. Fundamentals of Astrodynamics and Applications. 3
    ed. Microcosm Press, 2007.
    .. [2] http://celestrak.com/NORAD/documentation/tle-fmt.asp

    """
    l1_valid_start = int(l1[0]) == 1
    l2_valid_start = int(l2[0]) == 2

    l1_valid_length = len(l1) == 69
    l2_valid_length = len(l2) == 69

    l1_valid_checksum = int(l1[-1]) == checksum(l1)
    l2_valid_checksum = int(l2[-1]) == checksum(l2)
    return (l1_valid_start and l2_valid_start and
            l1_valid_length and l2_valid_length and
            l1_valid_checksum and l1_valid_checksum and l2_valid_checksum)


def checksum(line):
    r"""Compute checksum for a TLE line

    sum = checksum(line)

    Parameters
    ----------
    line : string
        A single line (string) from a TLE

    Returns
    -------
    sum : int
        The checksums for each line are calculated by adding the all numerical
        digits on that line, including the line number. One is added to the
        checksum for each negative sign (-) on that line. All other non-digit
        characters are ignored.  @note this excludes last char for the checksum
        thats already there.

    Note
    ----
    Input the line as is, no need to convert to float or anything

    Author
    ------
    Shankar Kulumani		GWU		skulumani@gwu.edu

    """
    L = line.strip()
    cksum = 0
    for i in range(68):
        c = L[i]
        if c <= '9' and c >= '0':
            cksum = cksum + int(c)
        elif c == '-':
            cksum = cksum + 1
        else:
            continue

    cksum = cksum % 10

    return cksum

def stringScientificNotationToFloat(sn):
    r"""TLE Scientific notation converter

    num = stringScientificNotationToFloat(sn)

    Parameters
    ----------
    sn : string
        String from a TLE 

    Returns
    -------
    num : float
        Output the string as a float

    Author
    ------
    Shankar Kulumani		GWU		skulumani@gwu.edu

    References
    ----------
    Specific format is 5 digits, a + or -, and 1 digit, ex: 01234-5 which is
    0.01234e-5

    Examples
    --------
    An example of how to use the function

    >>> sn = '012345-5'
    >>> stringScientificNotationToFloat(sn)
    0.01234e-5
    """ 

    return 1e-5 * float(sn[:6]) * 10**int(sn[6:])

def get_tle(filename):
    r"""Read TLEs from a file and save to a list

    all_tles = get_tle(filename)

    Parameters
    ----------
    filename : string
        Path to a text file to read. The file should only contain 
        the three-lines for each TLE. No extra white space 

    Returns
    -------
    all_tles : list
        List of TLE elements from all satellites contained inside filename
        Each element of the list is a TLE named tuple. The tuple is defined above.

    See Also
    --------
    parsetle : this actually reads and process the three lines of the TLE

    Author
    ------
    Shankar Kulumani		GWU		skulumani@gwu.edu
    """ 
    tles = 0
    lines = 0
    all_tles = []
    with open(filename, 'r') as f:
        l0 = f.readline().strip()
        while l0:
            l1 = f.readline().strip()
            lines += 1
            l2 = f.readline().strip()
            lines += 1
            # error check to make sure we have read a complete TLE
            if validtle(l0, l1, l2):
                # now we parse the tle
                elements = parsetle(l0, l1, l2)
                tles += 1
                # final check to see if we got a good TLE
                if elements.good:
                    # instantiate a bunch of instances of a Satellite class
                    all_tles.append(elements)

            else:
                print("Invalid TLE")

            l0 = f.readline().strip()
            lines += 1

    print("Read {} lines which should be {} TLEs".format(lines, lines / 3))
    print("Found {} TLEs".format(len(all_tles)))
    return all_tles


