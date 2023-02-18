"""
Docstring
"""

from volpy.velocities.generate_vimp_dist import calculate_relative_velocity, calculate_escape_velocity, generate_vimp_dist
import numpy as np
import pytest


def test_calculate_relative_velocity():
    """
    Docstring
    """

    v_rel_299 = calculate_relative_velocity(tiss=2.99,
                                        M_star=1.,
                                        a_pl=1.,
                                        G=6.67e-11,
                                        AU=1.496e11,
                                        M_solar=1.989e30)
    v_rel_3 = calculate_relative_velocity(tiss=3.,
                                        M_star=1.,
                                        a_pl=1.,
                                        G=6.67e-11,
                                        AU=1.496e11,
                                        M_solar=1.989e30)

    with pytest.raises(TypeError) as e_info:
        v_rel = calculate_relative_velocity(tiss=np.linspace(2., 3., 100),
                                            M_star=1.,
                                            a_pl=1.,
                                            G=6.67e-11,
                                            AU=1.496e11,
                                            M_solar=1.989e30)

    with pytest.raises(TypeError) as e_info:
        v_rel = calculate_relative_velocity(tiss=2.99,
                                            M_star=1,
                                            a_pl=1.,
                                            G=6.67e-11,
                                            AU=1.496e11,
                                            M_solar=1.989e30)

    with pytest.raises(TypeError) as e_info:
        v_rel = calculate_relative_velocity(tiss=2.99,
                                            M_star=1.,
                                            a_pl=1,
                                            G=6.67e-11,
                                            AU=1.496e11,
                                            M_solar=1.989e30)

    with pytest.raises(TypeError) as e_info:
        v_rel = calculate_relative_velocity(tiss=2.99,
                                            M_star=1.,
                                            a_pl=1,
                                            G=6.67e-11,
                                            AU='AU',
                                            M_solar=1.989e30)

    with pytest.raises(TypeError) as e_info:
        v_rel = calculate_relative_velocity(tiss=2.99,
                                            M_star=1,
                                            a_pl=1.,
                                            G=6.67e-11,
                                            AU=1.496e11,
                                            M_solar=1)

    assert v_rel_299, v_rel_3
    assert np.isclose(v_rel_299 / 1e3, 29.779 * np.sqrt(3 - 2.99), rtol=1e-4)
    assert v_rel_3 == 0


def test_calculate_escape_velocity():
    """
    Docstring
    """

    v_esc_earth = calculate_escape_velocity(M_pl=3.00273e-6,
                                            R_pl=4.2635e-5,
                                            G=6.67e-11,
                                            AU=1.496e11,
                                            M_solar=1.989e30)
    v_esc_mars = calculate_escape_velocity(M_pl=3.00273e-6 * 0.107,
                                            R_pl=4.2635e-5 * 0.53,
                                            G=6.67e-11,
                                            AU=1.496e11,
                                            M_solar=1.989e30)

    assert v_esc_earth
    assert np.isclose(v_esc_earth / 1e3, 11.176, rtol=1e-4)
    assert v_esc_mars < v_esc_earth


def test_generate_vimp_dist():
    """
    Docstring
    """

    with pytest.raises(TypeError) as e_info:
        v_imp = generate_vimp_dist(tiss_params=[1, 2, 3, 4],
                                   M_star=1,
                                   M_pl=3.00e-6,
                                   R_pl=4.26e-5,
                                   a_pl=1.,
                                   G=6.67e-11,
                                   AU=1.496e11,
                                   M_solar=1.989e30)

    v_imp = generate_vimp_dist(tiss_params=np.array([3.]),
                               M_star=1.,
                               M_pl=3.00e-6,
                               R_pl=4.26e-5,
                               a_pl=1.,
                               G=6.67e-11,
                               AU=1.496e11,
                               M_solar=1.989e30)
    v_esc = calculate_escape_velocity(M_pl=3.00e-6,
                                      R_pl=4.26e-5,
                                      G=6.67e-11,
                                      AU=1.496e11,
                                      M_solar=1.989e30)

    tiss_params = np.linspace(2., 2.999, 1000)
    v_imp_2 = generate_vimp_dist(tiss_params=tiss_params,
                                 M_star=1.,
                                 M_pl=3.00e-6,
                                 R_pl=4.26e-5,
                                 a_pl=1.,
                                 G=6.67e-11,
                                 AU=1.496e11,
                                 M_solar=1.989e30)

    assert v_imp
    assert v_imp[0] == v_esc
    assert len(v_imp_2) == len(tiss_params)
