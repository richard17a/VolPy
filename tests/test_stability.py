"""
Docstring
"""

import pytest # pylint: disable=import-error
import numpy as np # pylint: disable=import-error
from volpy.velocities.stability import calculate_max_num_planets
from volpy.habitable import calculate_habitable_zone
from volpy.snowline import calculate_snowline
from volpy.planet import Planet
from volpy.star import Star


def test_calculate_max_num_planets():
    """
    Docstring
    """
    mass = np.logspace(-1, 0, 1000)

    habitable_zone = calculate_habitable_zone(mass=mass)
    snow_line = calculate_snowline(mass=mass)

    earth = Planet(mass=3.00e-6,
                   radius=4.26e-5,
                   semimajor_axis=1.)
    sun = Star(mass=1.)

    max_num1 = calculate_max_num_planets(habitable_zone=habitable_zone[-1],
                                         snow_line=snow_line[-1],
                                         star=sun,
                                         planet=earth)
    max_num01 = calculate_max_num_planets(habitable_zone=habitable_zone[0],
                                          snow_line=snow_line[0],
                                          star=sun,
                                          planet=earth,
                                          conservative=True)

    with pytest.raises(TypeError):
        calculate_max_num_planets(habitable_zone=habitable_zone,
                                  snow_line=snow_line[-1],
                                  star=sun,
                                  planet=earth)
    with pytest.raises(TypeError):
        calculate_max_num_planets(habitable_zone=habitable_zone[-1],
                                  snow_line=snow_line[-1],
                                  star=sun,
                                  planet=earth,
                                  conservative=1)

    assert max_num1
    assert isinstance(max_num1, int)
    assert max_num01 > max_num1
