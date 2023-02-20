"""
Docstring
"""

import numpy as np # pylint: disable=import-error
import matplotlib.pyplot as plt # pylint: disable=import-error
from volpy.velocities.orbital_elements import calculate_tisserand
from volpy.velocities.generate_vimp_dist import calculate_min_vimp
from volpy.habitable import calculate_habitable_zone
from volpy.snowline import calculate_snowline
from volpy.planet import Planet
from volpy.star import Star


def main():
    """
    Docstring
    """

    stellar_mass = np.logspace(-1, 0, 1000)

    habitable_zone = calculate_habitable_zone(mass=stellar_mass)
    snow_line = calculate_snowline(mass=stellar_mass)

    mass_earth = 3.00e-6
    radius_earth = 4.26e-5
    earth = Planet(mass=mass_earth,
                   radius=radius_earth,
                   semimajor_axis=1.)

    tiss_1 = []
    vmin_1 = []
    tiss_2 = []
    vmin_2 = []
    tiss_3 = []
    vmin_3 = []
    tiss_5 = []
    vmin_5 = []

    for i, mass in enumerate(stellar_mass):

        tiss_1 = np.append(tiss_1, calculate_tisserand(habitable_zone=habitable_zone[i],
                                                       snow_line=snow_line[i],
                                                       num_planets=1))
        vmin_1 = np.append(vmin_1,
                           calculate_min_vimp(tiss=calculate_tisserand(
                                                        habitable_zone=habitable_zone[i],
                                                        snow_line=snow_line[i],
                                                        num_planets=1
                                                    ),
                                              star=Star(mass=mass),
                                              planet=Planet(mass=mass_earth,
                                                            radius=radius_earth,
                                                            semimajor_axis=habitable_zone[i]
                                                            )) / 1e3)

        tiss_2 = np.append(tiss_2, calculate_tisserand(habitable_zone=habitable_zone[i],
                                                       snow_line=snow_line[i],
                                                       num_planets=2))
        vmin_2 = np.append(vmin_2,
                           calculate_min_vimp(tiss=calculate_tisserand(
                                                        habitable_zone=habitable_zone[i],
                                                        snow_line=snow_line[i],
                                                        num_planets=2
                                                    ),
                                              star=Star(mass=mass),
                                              planet=Planet(mass=mass_earth,
                                                            radius=radius_earth,
                                                            semimajor_axis=habitable_zone[i]
                                                            )) / 1e3)

        tiss_3 = np.append(tiss_3, calculate_tisserand(habitable_zone=habitable_zone[i],
                                                       snow_line=snow_line[i],
                                                       num_planets=3))
        vmin_3 = np.append(vmin_3,
                           calculate_min_vimp(tiss=calculate_tisserand(
                                                        habitable_zone=habitable_zone[i],
                                                        snow_line=snow_line[i],
                                                        num_planets=3
                                                    ),
                                              star=Star(mass=mass),
                                              planet=Planet(mass=mass_earth,
                                                            radius=radius_earth,
                                                            semimajor_axis=habitable_zone[i]
                                                            )) / 1e3)

        tiss_5 = np.append(tiss_5, calculate_tisserand(habitable_zone=habitable_zone[i],
                                                       snow_line=snow_line[i],
                                                       num_planets=5))
        vmin_5 = np.append(vmin_5,
                           calculate_min_vimp(tiss=calculate_tisserand(
                                                        habitable_zone=habitable_zone[i],
                                                        snow_line=snow_line[i],
                                                        num_planets=5
                                                    ),
                                              star=Star(mass=mass),
                                              planet=Planet(mass=mass_earth,
                                                            radius=radius_earth,
                                                            semimajor_axis=habitable_zone[i]
                                                            )) / 1e3)

    plt.plot(stellar_mass, tiss_1, label=r'$N_\mathrm{pl} = 1$')
    plt.plot(stellar_mass, tiss_2, label=r'$N_\mathrm{pl} = 2$')
    plt.plot(stellar_mass, tiss_3, label=r'$N_\mathrm{pl} = 3$')
    plt.plot(stellar_mass, tiss_5, label=r'$N_\mathrm{pl} = 5$')
    plt.xscale('log')
    plt.xlabel(r'$M_\ast/M_\odot$')
    plt.ylabel('Tisserand parameter')
    plt.legend()
    plt.show()

    plt.plot(stellar_mass, vmin_1, label=r'$N_\mathrm{pl} = 1$')
    plt.plot(stellar_mass, vmin_2, label=r'$N_\mathrm{pl} = 2$')
    plt.plot(stellar_mass, vmin_3, label=r'$N_\mathrm{pl} = 3$')
    plt.plot(stellar_mass, vmin_5, label=r'$N_\mathrm{pl} = 5$')
    plt.axhline(earth.calculate_escape_velocity() / 1e3, ls='--', c='tab:gray')
    plt.xscale('log')
    plt.xlabel(r'$M_\ast/M_\odot$')
    plt.ylabel('Minimum impact velocity [km/s]')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
