"""
Module docstring
"""

import numpy as np # pylint: disable=import-error


def calc_luminosity(mass: np.ndarray):
    """
    Calculate the luminosity for a given array of stellar masses.

    Args:
        mass (np.ndarray): An array of stellar masses.

    Returns:
        np.ndarray: The calculated luminosity values for the given stellar masses.

    Raises:
        TypeError: If mass is not a numpy array.
        ValueError: If the maximum stellar mass exceeds 3 M_sun.
    """
    if not isinstance(mass, np.ndarray):
        raise TypeError('Stellar masses must be a numpy array.')
    if np.max(mass) > 3.:
        raise ValueError('Stellar masses cannot exceed 3 M_sun.')

    if np.max(mass) <= 1.:

        log_lum = 4.101 * (np.log10(mass[mass <=1]) ** 3) +\
                  8.162 * (np.log10(mass[mass <=1]) ** 2) +\
                  7.108 * (np.log10(mass[mass <=1]) ** 1) + 0.065

        lum = 10 ** log_lum

    else:

        log_lum = 4.101 * (np.log10(mass[mass <=1]) ** 3) +\
                  8.162 * (np.log10(mass[mass <=1]) ** 2) +\
                  7.108 * (np.log10(mass[mass <=1]) ** 1) + 0.065

        lum = []
        lum = np.append(lum, 10 ** log_lum)
        lum = np.append(lum, 10 ** log_lum[-1] * mass[np.where( (mass > 1) & (mass <= 3) )] ** 4.)

    return lum
