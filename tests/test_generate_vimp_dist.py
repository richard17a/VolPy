"""
Docstring
"""

import numpy as np # pylint: disable=import-error
import pytest # pylint: disable=import-error
from volpy.velocities.generate_vimp_dist import (calculate_relative_velocity,
                                                 generate_vimp_dist)
from volpy.planet import Planet
from volpy.star import Star


def test_calculate_relative_velocity():
    """
    Docstring
    """

    planet = Planet(mass=3.00e-6,
                    radius=4.26e-5,
                    semimajor_axis=1.)
    star = Star(mass=1.)

    v_rel_299 = calculate_relative_velocity(tiss=2.99,
                                            star=star,
                                            planet=planet)
    v_rel_3 = calculate_relative_velocity(tiss=3.,
                                          star=star,
                                          planet=planet)

    with pytest.raises(TypeError):
        calculate_relative_velocity(tiss=np.linspace(2., 3., 100),
                                    star=star,
                                    planet=planet)

    with pytest.raises(TypeError):
        calculate_relative_velocity(tiss=2.99,
                                    star=1.989e30,
                                    planet=planet)

    with pytest.raises(TypeError):
        calculate_relative_velocity(tiss=2.99,
                                    star=star,
                                    planet=3.00e-6)

    assert v_rel_299, v_rel_3
    assert np.isclose(v_rel_299 / 1e3, 29.785 * np.sqrt(3 - 2.99), rtol=1e-4)
    assert v_rel_3 == 0


def test_generate_vimp_dist():
    """
    Docstring
    """

    star = Star(mass=1.)
    planet = Planet(mass=3.00e-6,
                    radius=4.26e-5,
                    semimajor_axis=1.)

    with pytest.raises(TypeError):
        v_imp = generate_vimp_dist(tiss_params=[1, 2, 3, 4],
                                   star=star,
                                   planet=planet)

    v_imp = generate_vimp_dist(tiss_params=np.array([3.]),
                               star=star,
                               planet=planet)
    v_esc = planet.calculate_escape_velocity()

    tiss_params = np.linspace(2., 2.999, 1000)
    v_imp_2 = generate_vimp_dist(tiss_params=tiss_params,
                                 star=star,
                                 planet=planet)

    assert v_imp
    assert v_imp[0] == v_esc
    assert len(v_imp_2) == len(tiss_params)
