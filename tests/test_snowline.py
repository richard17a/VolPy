"""
Docstring
"""

import pytest # pylint: disable=import-error
import numpy as np # pylint: disable=import-error
from volpy.snowline import calculate_snowline


def test_calculate_snowline():
    """
    Docstring
    """

    mass = np.logspace(-1, np.log10(3), 1000)
    snowline = calculate_snowline(mass=mass)

    snowline_2 = calculate_snowline(mass=mass,
                                    inner=4.,
                                    outer=5.)

    snowline_3, inner, outer = calculate_snowline(mass=mass,
                                                  output_lims=True)

    with pytest.raises(TypeError):
        calculate_snowline(mass=[1, 2, 3, 4])

    with pytest.raises(ValueError):
        calculate_snowline(mass=np.array([1, 2, 3, 4]))

    with pytest.raises(ValueError):
        calculate_snowline(mass=np.array([1, 2, 3, 4]),
                           inner=10.,
                           outer=3.)

    with pytest.raises(TypeError):
        calculate_snowline(mass=np.array([1, 2, 3]),
                           inner=2.5,
                           outer=3)

    assert len(snowline) == len(mass)
    assert (snowline[676] > 2.5) &\
           (snowline[676] < 3.2)

    assert len(snowline_2) == len(mass)
    assert (snowline_2[676] > 4.) &\
           (snowline_2[676] < 5.)

    assert len(snowline_3) == len(mass)
    assert len(snowline_3) == len(inner)
    assert len(inner) == len(outer)
