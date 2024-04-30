# Filtered-IE23
Filtered-IE23 is an adaptive, filtered Implicit Euler method which uses a 2nd/3rd order embedded pair. This guide uses micromamba (https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) for the build. It will need to be installed on the target system before following the setup instructions below. If the user prefers conda, the environment yaml file should be compatible.

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

