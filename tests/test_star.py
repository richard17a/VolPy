"""
Docstring
"""

import pytest
from volpy.star import Star

def test_star():
    """
    Docstring
    """

    star_1 = Star(mass=1.)
    star_2 = Star(mass=.5)

    assert star_1
    assert star_1.mass == 1.
    assert star_1.radius == 1.

    assert star_2
    assert star_2.mass == .5
    assert star_2.radius == .5 ** .8


def test_star_setters():
    """
    Docstring
    """

    with pytest.raises(TypeError):
        Star(mass=1)
