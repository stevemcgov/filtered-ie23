# Filtered-IE23
Filtered-IE23 is an adaptive, filtered method based on Implicit Euler. It uses a 2nd/3rd order embedded pair for the variable step. This guide uses micromamba (https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) for the build. It will need to be installed on the target system before following the setup instructions below.

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

