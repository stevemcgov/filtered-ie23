# Filtered-IE23
Filtered-IE23 is an adaptive, filtered method based on Implicit Euler. It uses a 2nd/3rd order embedded pair for the variable step. The math behind this adaptive numerical code was part of my Master's Thesis:

McGovern, S.M. Numerical analysis, testing and adaptive timestep consideration for filtered
implicit methods. University of Pittsburgh Electronic Theses and Dissertations, Jan. 2023,
http://d-scholarship.pitt.edu/43968/.

The adaptive time stepping idea in particular was later published here:

McGovern, S.M. Adaptive Step Selection for a Filtered Implicit Method. J Sci Comput 103, 54 (2025). https://doi.org/10.1007/s10915-025-02861-w

This repository contains a Python implementation of the numerical method. In order to run the code, we first build an environment for the dependecies and then install the Python package `filtered_ie23_py`.

The guide uses [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) to build the required Python virtual environment. So `micromamba` will need to be installed on the target system before following the setup instructions below. Instructions on how to install micromamba [can be found here](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html).

If the user prefers conda, the environment yaml file should be compatible. However, the `install_env.sh` script is specific to micromamba.

## Create the Micromamba Environment
```
./install_env.sh
```

## Activate the Micromamba Environment
```
micromamba activate ./micromambaenv
```

## Install the package filtered_ie23_py
```
pip install .
```

## Run Numerical Tests
The numerical tests can be found in `filtered_ie23_py/numerical_tests`. Run with
```
python run_{TEST_NAME_HERE}
```

## Run the format tests
```
pytest test -v
```