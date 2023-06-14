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
    Calculate the relative velocity between a comet and a habitable planet based
    on the comet's Tisserand parameter.

    Parameters:
    - tiss (float): The Tisserand parameter.
    - star (Star): A Star object representing the central star.
    - planet (Planet): A Planet object representing the habitable planet.

    Returns:
    - v_rel (float): The relative velocity between the particle and planet.

    Formula (see paper):
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


def calculate_min_vimp(tiss: float,
                       star: Star,
                       planet: Planet):
    """
    Calculate the minimum impact velocity of the comet based on its Tisserand parameter

    Parameters:
    - tiss (float): The comet's Tisserand parameter.
    - star (Star): A Star object representing the central star.
    - planet (Planet): A Planet object representing the habitable planet.

    Returns:
    - v_imp (float): The minimum impact velocity onto the habitable planet.

    Formula (see paper):
    v_imp = sqrt(v_esc^2 + v_rel^2)
    """

    if not isinstance(tiss, float):
        raise TypeError('Tisserand paramter must be a float for the minimum velocity calculation.')
    if not isinstance(star, Star):
        raise TypeError('A Star object is required for the minimum velocity calculation.')
    if not isinstance(planet, Planet):
        raise TypeError('A Planet object is required for the minimum velocity calculation.')

    v_rel = calculate_relative_velocity(tiss=tiss,
                                        star=star,
                                        planet=planet)
    v_esc = planet.calculate_escape_velocity()
    v_imp = np.sqrt(v_esc ** 2 + v_rel ** 2)

    return v_imp


def generate_vimp_dist(tiss_params: np.ndarray,
                       star: Star,
                       planet: Planet):
    """
    Generate the impact velocity distribution for a given set of Tisserand parameters.

    Parameters:
    - tiss_params (np.ndarray): An array of Tisserand parameters.
    - star (Star): A Star object representing the central star.
    - planet (Planet): A Planet object representing the planet.

    Returns:
    - v_imp (np.ndarray): The array of impact velocities corresponding to the Tisserand parameters.

    Formula:
    v_imp = sqrt(v_esc^2 + v_rel^2)
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
