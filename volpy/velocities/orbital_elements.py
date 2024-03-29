"""
Docstring
"""

import numpy as np # pylint: disable=import-error
from volpy.planet import Planet
from volpy.star import Star


def calculate_eccentricity(habitable_zone: float,
                           snow_line: float,
                           num_planets: int):
    """
    Calculate the eccentricity of a particle assuming equally spaced planets
    between the habitable zone and snow line.

    Parameters:
    -----------
    habitable_zone : float
        Distance of the habitable zone from the star.
    snow_line : float
        Distance of the snow line from the star.
    num_planets : int
        Number of planets between the habitable zone and snow line.

    Returns:
    --------
    float
        Eccentricity of the particle.
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
    Calculate the semi-major axis of the particle's orbit assuming equally
    spaced planets between the habitable zone and snow line.

    Parameters:
    -----------
    habitable_zone : float
        Distance of the habitable zone from the star.
    snow_line : float
        Distance of the snow line from the star.
    num_planets : int
        Number of planets between the habitable zone and snow line.

    Returns:
    --------
    float
        Semi-major axis of the particle's orbit
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
    Calculate the Tisserand parameter of the particle assuming equally
    spaced planets between the habitable zone and snow line.

    Parameters:
    -----------
    habitable_zone : float
        Distance of the habitable zone from the star.
    snow_line : float
        Distance of the snow line from the star.
    num_planets : int
        Number of planets between the habitable zone and snow line.

    Returns:
    --------
    float
        Tisserand parameter of the particle.
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


def calculate_tisserand_hill_spacing(habitable_zone: float,
                                     planet: Planet,
                                     star: Star,
                                     delta_planet: float):
    """
    Calculate the particle's Tisserand parameter given a planetary separation
    delta_planet.

    Parameters:
    -----------
    habitable_zone : float
        Distance of the habitable zone from the star.
    planet : Planet object
        The planet object representing the planet.
    star : Star object
        The star object representing the central star.
    delta_planet : float
        Separation of planets (in mutual Hill raddii)

    Returns:
    --------
    float
        Tisserand parameter of the particle.
    """
    if not isinstance(habitable_zone, float):
        raise TypeError('Habitable zone distance must be a float.')
    if not isinstance(planet, Planet):
        raise TypeError('You must input a Planet object.')
    if not isinstance(star, Star):
        raise TypeError('You must input a Star object.')

    reduced_mass = (2 * planet.mass / 3 / star.mass) ** (1./3.) / 2

    tiss = (1 - delta_planet * reduced_mass) + 2 * np.sqrt( 1 + delta_planet * reduced_mass )

    return tiss
