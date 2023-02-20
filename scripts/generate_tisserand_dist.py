"""
Docstring
"""

import numpy as np # pylint: disable=import-error
import matplotlib.pyplot as plt # pylint: disable=import-error
from volpy.velocities.orbital_elements import (calculate_eccentricity,
                                               calculate_semimajor_axis,
                                               calculate_tisserand)
from volpy.habitable import calculate_habitable_zone
from volpy.snowline import calculate_snowline


def main():
    """
    Docstring
    """
    mass = np.logspace(-1, 0, 1000)

    habitable_zone = calculate_habitable_zone(mass=mass)
    snow_line = calculate_snowline(mass=mass)

    num_planets = np.linspace(1, 7, 7)

    ecc = []
    for num in num_planets:

        ecc = np.append(ecc, calculate_eccentricity(habitable_zone=habitable_zone[-1],
                                                    snow_line=snow_line[-1],
                                                    num_planets=int(num)))

    sma = []
    for num in num_planets:

        sma = np.append(sma, calculate_semimajor_axis(habitable_zone=habitable_zone[-1],
                                                      snow_line=snow_line[-1],
                                                      num_planets=int(num)))

    tiss = []
    for num in num_planets:

        tiss = np.append(tiss, calculate_tisserand(habitable_zone=habitable_zone[-1],
                                                   snow_line=snow_line[-1],
                                                   num_planets=int(num)))

    plt.plot(num_planets, sma, marker='.')
    plt.axhline(habitable_zone[-1], ls='--', c='tab:gray')
    plt.xlabel(r'$N_\mathrm{pl}$')
    plt.ylabel(r'$a_\mathrm{n}$')
    plt.show()

    plt.plot(num_planets, ecc, marker='.')
    plt.xlabel(r'$N_\mathrm{pl}$')
    plt.ylabel(r'$e_\mathrm{n}$')
    plt.show()

    plt.plot(num_planets, tiss, marker='.')
    plt.xlabel(r'$N_\mathrm{pl}$')
    plt.ylabel(r'$\mathcal{T}_\mathrm{n}$')
    plt.show()


if __name__ == "__main__":
    main()
