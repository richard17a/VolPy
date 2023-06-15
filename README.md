[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Tests](https://github.com/richard17a/VolPy/actions/workflows/python-package.yml/badge.svg)

# VolPy

This repository contains the REBOUND scripts used for the N-body test particle simulations, as well as simple scripts to generate the figures found in Anslow, Bonsor & Rimmer 2023, submitted (Proceedings of the Royal Society A).

**Important** 
The Makefile's for the REBOUND (https://github.com/hannorein/rebound) N-body simulations currently have a dummy path (./path_to_rebound_src/), which should be replaced with your local path to the REBOUND src/ directory.

## Setup
- Install the package from Github
- Navigate to project directory
- Install required packages
	- pip install -r requirements.txt
- Install the package
	- pip install .

## Generate figures from paper
- navigate to paper_figures/ directory
- python figure_x.py

## Run the N-body simulations
- navigate to rebound_scripts/ directory. Each subfolder (e.g. Gtype_delta10/) corresponds to a individual simulation run (in this case it is for a 1M_Sun star, with interplanetary spacing 10 mutual Hill radii).
- navigate to subfolder - cd Gtype_delta10/
- make
- ./rebound