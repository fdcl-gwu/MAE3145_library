"""This script is what we'll use to interface with our program and functions.

From here we'll:
    Import our various functions
    Setup any parameters/constants that we need to input to the functions
    Accept and analyze the outputs of our functions
    Plot any data or otherwise output for us to use

All of the 'real' work should happen in your packages, modules or functions. 

As a result this script shouldn't be that long or complicated, as all the specific operations should be placed into an appropriate function

"""

import numpy as np
import matplotlib.pyplot as plt

from astro import example_module

print("Let's add two numbers")

a = input("What is the first number? ")
b = input("What is the second number? ")

c = example_module.add_two_inputs(float(a), float(b))

print("The sum is %4.2f" % c)
