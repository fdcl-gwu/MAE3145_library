# MAE3145_library

Library of some astro functions for MAE3145

## Installation

First we need to ensure that the code is the same across systems.

0. You should have already installed [Anaconda](https://www.anaconda.com/download/) 

    * Ensure you download the Python 3 version for your system

1. Get this library onto your system. Github provides a clone or download link you can use. 
It is preferrable to use `git` to manage this library but if you choose not to, you can download the zip files from

    * [Library](https://github.com/fdcl-gwu/MAE3145_library/archive/master.zip)

    Extract the zip file to a good directory and navigate into this directory - `cd path/to/MAE3145_library`.
    Inside this directory, the file structure should look similar to this:

    ~~~
    ├── astro
    │   ├── constants.py
    │   ├── example_module.py
    │   ├── __init__.py
    │   ├── tests
    │   │   ├── __init__.py
    │   │   ├── test_constants.py
    │   │   └── test_time.py
    │   └── time.py
    ├── astro_win.yml
    ├── astro_unix.yml
    ├── data
    │   ├── RV1_solution.txt
    │   ├── RV1.txt
    │   ├── RV2COE_tle_rv.txt
    │   ├── RV2COE_tle_solution.txt
    │   └── vector.txt
    ├── example_driver.py
    ├── kinematics
    │   ├── attitude.py
    │   ├── __init__.py
    │   ├── LICENSE.md
    │   ├── README.md
    │   ├── setup_repo.sh
    │   ├── sphere.py
    │   ├── tags
    │   └── tests
    │       ├── __init__.py
    │       ├── test_attitude.py
    │       └── test_sphere.py
    ├── LICENSE.md
    ├── README.md
    ├── tags
    └── tests
        ├── __init__.py
        └── test_example_module.py
    ~~~

2. Open Ipython - the Anaconda software gives you a nice ability to easily open Python. 
Instructions will differ based on your system

    * Windows - Go to Start and search for `Ipython`
    * MacOS - Open the `Terminal` app and type `ipython` to start Python

3. Next, you should make sure the library is working properly by testing. 

    * Navigate to the correct directory - `cd path/to/MAE3145_library`

    From this directory you can run the tests using `pytest`

4. Congratulations, you have the astro library and can begin adding your own functions and modules

### Keeping up with changes

You now have the astro library and it is working properly. 
You are encouraged to use this library in your homework/project assignments. 
Furthermore, you are HIGHLY encouraged to use `git` to ensure you have the most up-to-date version of this library and keep track of your additions. 

The steps to use `git` are best summarized below:

* [Setup Git](https://help.github.com/articles/set-up-git/)
* [Fork the repo](https://help.github.com/articles/fork-a-repo/) - create your own copy

Without `git` you'll need to manually verify that you have the most up to date version of these files.

## Function listing

The astrodynamic functions are contained in the `astro` package.
 
* `astro.time` - Module which contains time related transformations and operations
* `astro.constants` - A variety of planetary constants are saved in this module. 
For example, to get the radius of Jupiter

~~~
from astro import constants
print(constants.jupiter.radius)
~~~

The `kinematics` package holds several attitude transformation related functions.

## Suggestions for use/structure

