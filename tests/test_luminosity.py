"""
Docstring
"""

import pytest # pylint: disable=import-error
import numpy as np # pylint: disable=import-error
from volpy.luminosity import calc_luminosity


def test_calc_luminosity():
    """
    Docstring
    """

    mass = np.logspace(-1, np.log10(3), 1000)
    lum = calc_luminosity(mass=mass)

    with pytest.raises(TypeError):
        calc_luminosity(mass=[1, 2, 3, 4])

    with pytest.raises(ValueError):
        calc_luminosity(mass=np.array([1, 2, 3, 4]))

    assert len(lum) == len(mass)
