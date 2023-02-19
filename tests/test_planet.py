"""
Docstring
"""

import pytest
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
