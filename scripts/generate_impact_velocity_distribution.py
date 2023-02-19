"""
This demonstrates how to generate a velocity distribution for an arbitrary Tisserand parameter distribution.
"""

import numpy as np # pylint: disable=import-error
import matplotlib.pyplot as plt # pylint: disable=import-error
from volpy.velocities.generate_vimp_dist import generate_vimp_dist
from volpy.planet import Planet
from volpy.star import Star


def main():
    """
    docstring
    """

    tiss_params = np.linspace(2., 2.999, 10000)

    sun = Star(mass=1.)
    earth = Planet(mass=3.00e-6,
                   radius=4.26e-5,
                   semimajor_axis=1.)

    v_esc = earth.calculate_escape_velocity()

    v_imp = generate_vimp_dist(tiss_params=tiss_params,
                               star=sun,
                               planet=earth)

    plt.hist(v_imp / 1e3, bins=50, histtype='step', density=True)
    plt.axvline(v_esc / 1e3,
                ls='--',
                c='tab:gray',
                label=r'$v_\mathrm{esc}$')
    plt.xlabel('Impact velocity [km/s]')
    plt.ylabel('Frequency')
    plt.legend(loc='upper left')
    plt.show()


if __name__ == "__main__":
    main()
