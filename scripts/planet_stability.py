"""
Docstring
"""

import numpy as np # pylint: disable=import-error
import matplotlib.pyplot as plt # pylint: disable=import-error
from volpy.velocities.stability import calculate_max_num_planets
from volpy.habitable import calculate_habitable_zone
from volpy.snowline import calculate_snowline
from volpy.planet import Planet
from volpy.star import Star


def main():
    """
    Docstring
    """

    mass = np.logspace(-1, 0, 1000)

    habitable_zone = calculate_habitable_zone(mass=mass)
    snow_line = calculate_snowline(mass=mass)

    earth = Planet(mass=3.00e-6,
                   radius=4.26e-5,
                   semimajor_axis=1.)
    sun = Star(mass=1.)

    max_num = []

    for hab_zone, i in enumerate(habitable_zone):

        max_num = np.append(max_num,
                            calculate_max_num_planets(habitable_zone=hab_zone,
                                                      snow_line=snow_line[i],
                                                      star=sun,
                                                      planet=earth,
                                                      conservative=False))

    plt.plot(mass, max_num)
    plt.xlabel(r'$M_\ast/M_\odot$')
    plt.ylabel(r'$N_{\mathrm{pl}, \mathrm{max}}$')
    plt.show()


if __name__ == "__main__":
    main()
