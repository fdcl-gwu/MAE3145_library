# MAE3145_library

Library of some astro functions for MAE3145

## Installation

First we need to ensure that the code is the same across systems.

0. You should have already installed [Anaconda](https://www.anaconda.com/download/) 

* Ensure you download the Python 3 version for your system

1. Get this library onto your system. Github provides a clone or download link you can use. 
It is preferrable to use `git` to manage this library but if you choose not to, you can download the zip files from

* [Library](https://github.com/fdcl-gwu/MAE3145_library/archive/master.zip)
* [Kinematics](https://github.com/fdcl-gwu/kinematics/archive/00b1a485e3d6076bc98d2fa4e4ac506cd342b8b3.zip)

Extract both and then place the `kinematics` zip file contents into `MAE3145_library/kinematics`. Once completed your directory should look something like this:

~~~
├── astro
│   ├── constants.py
│   ├── example_module.py
│   ├── __init__.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   └── test_tle.cpython-36-PYTEST.pyc
│   │   ├── test_constants.py
│   │   └── test_time.py
│   └── time.py
├── astro_env.yml
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

2. [Anaconda environment](https://conda.io/docs/user-guide/tasks/manage-environments.html#) - we use a `conda` environment to ensure that the code requirements are the same across systems. 
This directory holds an `astro_env.yml` file which holds the required packages and software to run this code.
To recreate it on your own system simply open a terminal and run

~~~
conda env create -f astro_env.yml
~~~

Once complete, you should activate this environment using

* Windows - `activate astro`
* macOS/Linux - `source activate astro`

3. Next, you should make sure the library is working properly by testing. 

* Navigate to the correct directory - `cd path/to/MAE3145_library`

From this directory you can run the tests using `pytest`
A single function called `test_always_fail` should be the only failure.

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

- [ ] List and short description of included functions

## Suggestions for use/structure

- [ ] Use this with git, provide some links
- [ ] Make your own module for homeworks/projects
- [ ] Get FDCL to test it out
- [ ] Test on the lab computers and my laptop

