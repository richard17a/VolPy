"""
Docstring
"""

import numpy as np # pylint: disable=import-error
import matplotlib.pyplot as plt # pylint: disable=import-error
from volpy.habitable import calculate_habitable_zone


def main():
    """
    Docstring
    """
    mass = np.logspace(-1, np.log10(3), 1000)
    habitable, habitable_in, habitable_out = calculate_habitable_zone(mass=mass,
                                                                      output_lims=True)
    plt.plot(mass, habitable)
    plt.plot(mass, habitable_in, ls='--', c='tab:blue')
    plt.plot(mass, habitable_out, ls='--', c='tab:blue')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1e-1, 3)
    plt.xlabel(r'$M_\ast/M_\odot$')
    plt.xlabel(r'$R_\mathrm{HZ}$')
    plt.show()

if __name__ == "__main__":
    main()
