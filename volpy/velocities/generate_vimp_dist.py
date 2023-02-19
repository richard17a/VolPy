"""
Docstring
"""

import numpy as np # pylint: disable=import-error
from astropy import constants as const # pylint: disable=import-error
from volpy.planet import Planet
from volpy.star import Star


def calculate_relative_velocity(tiss: float,
                                star: Star,
                                planet: Planet):
    """
    Docstring

    v_rel = v_kep * sqrt(3 - Tiss)

    """

    if not isinstance(tiss, float):
        raise TypeError('Tisserand paramter must be a float for the relative velocity calculation.')
    if not isinstance(star, Star):
        raise TypeError('A Star object is required for the relative velocity calculation.')
    if not isinstance(planet, Planet):
        raise TypeError('A Planet object is required for the relative velocity calculation.')

    v_kep = np.sqrt((const.G.value * star.mass * const.M_sun.value) /
                    (planet.semimajor_axis * const.au.value))
    v_rel = v_kep * np.sqrt(3 - tiss)

    return v_rel


def generate_vimp_dist(tiss_params: np.ndarray,
                       star: Star,
                       planet: Planet):
    """
    Docstring
    """
    if not isinstance(tiss_params, np.ndarray):
        raise TypeError('Tisserand paramters must be in a numpy array for\
                         generating the impact velocity distribution.')
    if not isinstance(star, Star):
        raise TypeError('A Star object is required for generating the impact\
                         velocity distribution.')
    if not isinstance(planet, Planet):
        raise TypeError('A Planet object is required for generating the impact\
                         velocity distribution.')

    v_esc = planet.calculate_escape_velocity()

    v_imp = []

    for tiss in tiss_params:

        v_rel = calculate_relative_velocity(tiss=tiss,
                                            star=star,
                                            planet=planet)

        v_imp = np.append(v_imp, np.sqrt(v_esc ** 2 + v_rel ** 2))

    return v_imp
