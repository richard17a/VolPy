"""
Docstring
"""

import pytest # pylint: disable=import-error
import numpy as np # pylint: disable=import-error
from volpy.velocities.orbital_elements import (calculate_eccentricity,
                                               calculate_semimajor_axis,
                                               calculate_tisserand)
from volpy.habitable import calculate_habitable_zone
from volpy.snowline import calculate_snowline


def test_calculate_eccentricity():
    """
    Docstring
    """

    mass = np.logspace(-1, 0, 1000)

    habitable_zone = calculate_habitable_zone(mass=mass)
    snow_line = calculate_snowline(mass=mass)

    ecc_1 = calculate_eccentricity(habitable_zone=habitable_zone[-1],
                                   snow_line=snow_line[-1],
                                   num_planets=1)
    ecc_7 = calculate_eccentricity(habitable_zone=habitable_zone[-1],
                                   snow_line=snow_line[-1],
                                   num_planets=7)

    with pytest.raises(TypeError):
        calculate_eccentricity(habitable_zone=habitable_zone[-1],
                               snow_line=snow_line[-1],
                               num_planets=1.5)

    with pytest.raises(ValueError):
        calculate_eccentricity(habitable_zone=habitable_zone[-1] + snow_line[-1],
                               snow_line=snow_line[-1],
                               num_planets=1)

    with pytest.raises(TypeError):
        calculate_eccentricity(habitable_zone=habitable_zone,
                               snow_line=snow_line[-1],
                               num_planets=1)

    assert ecc_1, ecc_7
    assert ecc_7 < ecc_1
    assert (ecc_1 < 1.) & (ecc_7 < 1.) & (ecc_1 > 0) & (ecc_7 > 0)


def test_calculate_semimajor_axis():
    """
    Docstring
    """

    mass = np.logspace(-1, 0, 1000)

    habitable_zone = calculate_habitable_zone(mass=mass)
    snow_line = calculate_snowline(mass=mass)

    sma_1 = calculate_semimajor_axis(habitable_zone=habitable_zone[-1],
                                          snow_line=snow_line[-1],
                                          num_planets=1)
    sma_7 = calculate_semimajor_axis(habitable_zone=habitable_zone[-1],
                                          snow_line=snow_line[-1],
                                          num_planets=7)

    with pytest.raises(TypeError):
        calculate_semimajor_axis(habitable_zone=habitable_zone,
                                 snow_line=snow_line[-1],
                                 num_planets=1)

    with pytest.raises(TypeError):
        calculate_semimajor_axis(habitable_zone=habitable_zone[-1],
                                 snow_line=snow_line[-1],
                                 num_planets=1.)

    with pytest.raises(ValueError):
        calculate_semimajor_axis(habitable_zone=habitable_zone[-1] + snow_line[-1],
                                 snow_line=snow_line[-1],
                                 num_planets=1)

    assert sma_1, sma_7
    assert sma_1 > sma_7
    assert (sma_7 > habitable_zone[-1]) & (sma_7 < snow_line[-1])
    assert (sma_1 > habitable_zone[-1]) & (sma_1 < snow_line[-1])



def test_calculate_tisserand():
    """
    Docstring
    """

    mass = np.logspace(-1, 0, 1000)

    habitable_zone = calculate_habitable_zone(mass=mass)
    snow_line = calculate_snowline(mass=mass)

    tiss_1 = calculate_tisserand(habitable_zone=habitable_zone[-1],
                                      snow_line=snow_line[-1],
                                      num_planets=1)
    tiss_7 = calculate_tisserand(habitable_zone=habitable_zone[-1],
                                      snow_line=snow_line[-1],
                                      num_planets=7)

    with pytest.raises(TypeError):
        calculate_tisserand(habitable_zone=habitable_zone[-1],
                            snow_line=snow_line[-1],
                            num_planets=1.)

    with pytest.raises(ValueError):
        calculate_tisserand(habitable_zone=habitable_zone[-1] + snow_line[-1],
                            snow_line=snow_line[-1],
                            num_planets=1)

    assert tiss_1, tiss_7
    assert tiss_1 < tiss_7
