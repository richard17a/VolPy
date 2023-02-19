"""
Docstring
"""

import numpy as np # pylint: disable=import-error
import matplotlib.pyplot as plt # pylint: disable=import-error
from volpy.snowline import calculate_snowline


def main():
    """
    docstring
    """

    mass = np.logspace(-1, np.log10(3), 1000)
    snowline, snowline_in, snowline_out = calculate_snowline(mass=mass,
                                                             output_lims=True)

    plt.plot(mass, snowline)
    plt.plot(mass, snowline_in, ls='--', c='tab:blue')
    plt.plot(mass, snowline_out, ls='--', c='tab:blue')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1e-1, 3)
    plt.show()


if __name__ == "__main__":
    main()
