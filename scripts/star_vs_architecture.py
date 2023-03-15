"""
Docstring
"""

import numpy as np # pylint: disable=import-error
import matplotlib.pyplot as plt # pylint: disable=import-error
from volpy.habitable import calculate_habitable_zone
from volpy.snowline import calculate_snowline
from volpy.planet import Planet
from volpy.star import Star
from volpy.velocities.orbital_elements import (calculate_eccentricity,
                                               calculate_tisserand)
from volpy.velocities.generate_vimp_dist import generate_vimp_dist


def main():
    """
    Docstring
    """
    mass = np.logspace(-1, 0, 1000)
    habitables = calculate_habitable_zone(mass=mass,
                                          output_lims=True)
    snowlines = calculate_snowline(mass=mass,
                                   output_lims=True)

    habitable = habitables[0]
    snowline =snowlines[0]

    kdwarf = Star(mass=1.)
    mdwarf = Star(mass=.1)
    earth_m = Planet(mass=3.00e-6,
                     radius=4.26e-5,
                     semimajor_axis=habitable[0])
    earth_k = Planet(mass=3.00e-6,
                     radius=4.26e-5,
                     semimajor_axis=habitable[-1])

    num_planets = np.linspace(1, 7, 7)

    ecc_m = []
    ecc_k = []
    tiss_m = []
    tiss_k = []

    for num in num_planets:

        ecc_m = np.append(ecc_m, calculate_eccentricity(habitable_zone=habitable[0],
                                                        snow_line=snowline[0],
                                                        num_planets=int(num)))
        ecc_k = np.append(ecc_k, calculate_eccentricity(habitable_zone=habitable[-1],
                                                        snow_line=snowline[-1],
                                                        num_planets=int(num)))

        tiss_m = np.append(tiss_m, calculate_tisserand(habitable_zone=habitable[0],
                                                       snow_line=snowline[0],
                                                       num_planets=int(num)))
        tiss_k = np.append(tiss_k, calculate_tisserand(habitable_zone=habitable[-1],
                                                       snow_line=snowline[-1],
                                                       num_planets=int(num)))

    plt.plot(num_planets, tiss_m / max(tiss_m), marker='.', label='M dwarf')
    plt.plot(num_planets, tiss_k / max(tiss_k), marker='.', label='K dwarf')

    plt.title(f'max(M dwarf) = {max(tiss_m):.3f}, max(K dwarf) = {max(tiss_k):.3f}')
    plt.xlabel(r'$N_\mathrm{pl}$')
    plt.ylabel(r'$\mathcal{T} / \mathrm{max}(\mathcal{T})$')

    plt.legend(loc='lower right')

    plt.show()

    v_esc = earth_m.calculate_escape_velocity()

    v_imp_k = generate_vimp_dist(tiss_params=tiss_k,
                                 star=kdwarf,
                                 planet=earth_k)
    v_imp_m = generate_vimp_dist(tiss_params=tiss_m,
                                 star=mdwarf,
                                 planet=earth_m)

    plt.plot(num_planets, v_imp_m / 1e3, marker='.', label='M dwarf')
    plt.plot(num_planets, v_imp_k / 1e3, marker='.', label='K dwarf')
    plt.axhline(v_esc / 1e3, ls='--', c='tab:gray')

    plt.xlabel(r'$N_\mathrm{pl}$')
    plt.ylabel(r'$v_\mathrm{imp}$ [km/s]')

    plt.ylim(11, 16)

    plt.legend()

    plt.show()


    plt.plot((v_imp_m - v_imp_k) / v_imp_k, marker='.')

    plt.xlabel(r'$N_\mathrm{pl}$')
    plt.ylabel(r'$\Delta v / v_{\mathrm{imp}, k}$')

    plt.ylim(0,)

    plt.show()


if __name__ == "__main__":
    main()
