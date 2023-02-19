"""
Docstring
"""

import pytest # pylint: disable=import-error
import numpy as np # pylint: disable=import-error
from volpy.planet import Planet


def test_planet():
    """
    Docstring
    """

    planet_1 = Planet(mass=3.00e-6,
                      radius=4.26e-5,
                      semimajor_axis=1.)

    assert planet_1
    assert planet_1.mass == 3.00e-6
    assert planet_1.radius == 4.26e-5
    assert planet_1.semimajor_axis == 1.


def test_planet_setter():
    """
    Docstring
    """

    with pytest.raises(TypeError):
        Planet(mass=1,
               radius=2.,
               semimajor_axis=1.)

    with pytest.raises(TypeError):
        Planet(mass=1.,
               radius=2,
               semimajor_axis=1.)

    with pytest.raises(TypeError):
        Planet(mass=1.,
               radius=2.,
               semimajor_axis=1)

def test_calculate_escape_velocity():
    """
    Docstring
    """

    earth = Planet(mass=3.00e-6,
                   radius=4.26e-5,
                   semimajor_axis=1.)

    mars = Planet(mass=3.00e-6 * 0.107,
                  radius=4.26e-5 * 0.53,
                  semimajor_axis=1.524)

    v_esc_earth = earth.calculate_escape_velocity()
    v_esc_mars = mars.calculate_escape_velocity()

    assert v_esc_earth
    assert np.isclose(v_esc_earth / 1e3, 11.177, rtol=1e-4)
    assert v_esc_mars < v_esc_earth
