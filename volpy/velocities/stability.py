"""
Docstring
"""

import numpy as np # pylint: disable=import-error
from volpy.planet import Planet
from volpy.star import Star


def calculate_max_num_planets(habitable_zone: float,
                              snow_line: float,
                              star: Star,
                              planet: Planet,
                              conservative=True):
    """
    Docstring - this is for equal mass planets
    """
    if not isinstance(habitable_zone, float):
        raise TypeError('Habitable zone distance must be a float.')
    if not isinstance(snow_line, float):
        raise TypeError('Snow-line distance must be a float.')
    if not isinstance(planet, Planet):
        raise TypeError('The planet must be a Planet object.')
    if not isinstance(star, Star):
        raise TypeError('The star must be a Star object.')
    if not isinstance(conservative, bool):
        raise TypeError('Conservative flag must be a bool.')
    if habitable_zone > snow_line:
        raise ValueError('The snow-line should be outside of the habitable zone.')

    if conservative:
        delta_crit = 2 * 1.46 * ( (2 * planet.mass / 3 / star.mass) ** (-1./3.) ) ** (2./7.)
    else:
        delta_crit = 1.46 * ( (2 * planet.mass / 3 / star.mass) ** (-1./3.) ) ** (2./7.)


    num_planets = 2 * (snow_line - habitable_zone) *\
                  ( (2 * planet.mass / 3 / star.mass) ** (-1./3.) ) /\
                  (snow_line + habitable_zone) / delta_crit

    return int(np.floor(num_planets))
