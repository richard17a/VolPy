"""
Docstring
"""

import numpy as np # pylint: disable=import-error


def calculate_eccentricity(habitable_zone: float,
                           snow_line: float,
                           num_planets: int):
    """
    Docstring

    Assuming we have a planet at the habitable zone, and snow-line, equally spaced
    between.
    """
    if not isinstance(habitable_zone, float):
        raise TypeError('Habitable zone distance must be a float.')
    if not isinstance(snow_line, float):
        raise TypeError('Snow-line distance must be a float.')
    if not isinstance(num_planets, int):
        raise TypeError('The number of planets must be an integer.')
    if habitable_zone > snow_line:
        raise ValueError('The snow-line should be outside of the habitable zone.')

    ecc = (snow_line - habitable_zone) / (snow_line + (2 * num_planets - 1) * habitable_zone)

    return ecc


def calculate_semimajor_axis(habitable_zone: float,
                             snow_line: float,
                             num_planets: int):
    """
    Docstring
    """
    if not isinstance(habitable_zone, float):
        raise TypeError('Habitable zone distance must be a float.')
    if not isinstance(snow_line, float):
        raise TypeError('Snow-line distance must be a float.')
    if not isinstance(num_planets, int):
        raise TypeError('The number of planets must be an integer.')
    if habitable_zone > snow_line:
        raise ValueError('The snow-line should be outside of the habitable zone.')

    sma = (snow_line + (2 * num_planets - 1) * habitable_zone) / (2 * num_planets)

    return sma


def calculate_tisserand(habitable_zone: float,
                        snow_line: float,
                        num_planets: int):
    """
    Docstring
    """
    if not isinstance(habitable_zone, float):
        raise TypeError('Habitable zone distance must be a float.')
    if not isinstance(snow_line, float):
        raise TypeError('Snow-line distance must be a float.')
    if not isinstance(num_planets, int):
        raise TypeError('The number of planets must be an integer.')
    if habitable_zone > snow_line:
        raise ValueError('The snow-line should be outside of the habitable zone.')

    sma = calculate_semimajor_axis(habitable_zone=habitable_zone,
                                   snow_line=snow_line,
                                   num_planets=num_planets)
    ecc = calculate_eccentricity(habitable_zone=habitable_zone,
                                 snow_line=snow_line,
                                 num_planets=num_planets)

    tiss = habitable_zone / sma + 2 * np.sqrt(sma * (1 - ecc**2) / habitable_zone)

    return tiss
