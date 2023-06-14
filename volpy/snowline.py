"""
Module Docstring
"""

import numpy as np # pylint: disable=import-error
from volpy.luminosity import calc_luminosity


def calculate_snowline(mass: np.ndarray,
                       inner=2.5,
                       outer=3.2,
                       output_lims=False):
    """
    Calculate the snowline positions for a given array of stellar masses.

    Args:
        mass (np.ndarray): An array of stellar masses.
        inner (float, optional): The inner snowline position.
        outer (float, optional): The outer snowline position.
        output_lims (bool, optional): Whether to output the inner and outer
                                      snowline positions (default is False).

    Returns:
        np.ndarray or tuple: The snowline positions. If output_lims is False,
                             returns an array of snowline positions. If
                             output_lims is True, returns a tuple of
                             (snowline, snowline_in, snowline_out).

    Raises:
        TypeError: If mass is not a numpy array or inner/outer/output_lims
                   are not of the expected type.
        ValueError: If the maximum stellar mass exceeds 3 M_sun or if the
                    outer snowline is not outside the inner snowline.
    """
    if not isinstance(mass, np.ndarray):
        raise TypeError('Stellar masses must be a numpy array.')
    if np.max(mass) > 3.:
        raise ValueError('Stellar masses cannot exceed 3 M_sun.')
    if not isinstance(inner, float):
        raise TypeError('Inner snowline must be a float.')
    if not isinstance(outer, float):
        raise TypeError('Outer snowline must be a float.')
    if not isinstance(output_lims, bool):
        raise TypeError('Outer snowline must be True or False.')
    if outer <= inner:
        raise ValueError('Outer snowline must be outside inner snowline.')

    lum = calc_luminosity(mass=mass)

    nearest_index = min(range(len(mass)), key=lambda i: abs(mass[i]-1.))

    snowline_in = []
    snowline_in = np.append(snowline_in,
                            inner * (mass[mass <= 1] ** (1./3.)) *\
                            ((mass[mass <= 1] ** 1.81)) ** (4./9.))
    snowline_in = np.append(snowline_in,
                            snowline_in[-1] * ((lum[mass > 1] /\
                            lum[nearest_index]) ** 0.5))

    snowline_out = []
    snowline_out = np.append(snowline_out,
                             outer * (mass[mass <= 1] ** (1./3.)) *\
                             ((mass[mass <= 1] ** 1.81)) ** (4./9.))
    snowline_out = np.append(snowline_out,
                             snowline_out[-1] * ((lum[mass > 1] /\
                             lum[nearest_index]) ** 0.5))

    snowline = 0.5 * (snowline_in + snowline_out)

    if not output_lims:
        return snowline

    return snowline, snowline_in, snowline_out
