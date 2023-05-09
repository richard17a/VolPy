"""
Docstring
"""

import numpy as np # pylint: disable=import-error
import matplotlib.pyplot as plt # pylint: disable=import-error
import matplotlib # pylint: disable=import-error
from matplotlib.lines import Line2D # pylint: disable=import-error
from volpy.habitable import calculate_habitable_zone
from volpy.velocities.orbital_elements import calculate_tisserand_hill_spacing
from volpy.star import Star
from volpy.planet import Planet

matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'


def main():
    """
    Docstring
    """

    mass = np.logspace(-1, 0, 1000)

    m_earth = 3.00e-6
    r_earth = 4.26e-5

    habitable_out = calculate_habitable_zone(mass=mass,
                                             output_lims=True)

    habitable_zone = habitable_out[0]

    tisserand_10, tisserand_20, tisserand_30 = [], [], []
    for i in range(len(habitable_zone)):
        tisserand_10 = np.append(
                         tisserand_10,
                         calculate_tisserand_hill_spacing(
                                 habitable_zone=habitable_zone[i],
                                 planet=Planet(
                                            mass=m_earth,
                                            radius=r_earth,
                                            semimajor_axis=habitable_zone[i]
                                        ),
                                 star=Star(mass=mass[i]),
                                 delta_planet=10)
                       )
        tisserand_20 = np.append(
                         tisserand_20,
                         calculate_tisserand_hill_spacing(
                                 habitable_zone=habitable_zone[i],
                                 planet=Planet(
                                            mass=m_earth,
                                            radius=r_earth,
                                            semimajor_axis=habitable_zone[i]
                                        ),
                                 star=Star(mass=mass[i]),
                                 delta_planet=20)
                       )
        tisserand_30 = np.append(
                         tisserand_30,
                         calculate_tisserand_hill_spacing(
                                 habitable_zone=habitable_zone[i],
                                 planet=Planet(
                                            mass=m_earth,
                                            radius=r_earth,
                                            semimajor_axis=habitable_zone[i]
                                        ),
                                 star=Star(mass=mass[i]),
                                 delta_planet=30)
                       )

    theta = m_earth * habitable_zone / r_earth / mass

    sigma_A10 = (1 + 2 * theta / (3 - tisserand_10)) / habitable_zone ** 2
    sigma_A20 = (1 + 2 * theta / (3 - tisserand_20)) / habitable_zone ** 2
    sigma_A30 = (1 + 2 * theta / (3 - tisserand_30)) / habitable_zone ** 2

    plt.plot(mass, sigma_A10, label=r'$\Delta a = 10 R_{H,m}$')
    plt.plot(mass, sigma_A20, label=r'$\Delta a = 20 R_{H,m}$')
    plt.plot(mass, sigma_A30, label=r'$\Delta a = 30 R_{H,m}$')

    plt.plot(mass, 1 / habitable_zone ** 2, ls='--', c='tab:gray')

    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(r'$M_\ast [M_\mathrm{Sun}]$', fontsize=13)
    plt.ylabel(r'$\frac{\sigma_\mathrm{acc}}{R_\mathrm{pl}^2a_\mathrm{pl}^2}$', rotation=0, labelpad=15, fontsize=13)

    plt.legend(borderpad=0.5)

    # plt.savefig('collision_cross_section.pdf', format='pdf', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
