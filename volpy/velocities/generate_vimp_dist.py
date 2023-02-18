"""
Docstring
"""

import numpy as np


def calculate_relative_velocity(tiss: float,
                                m_star: float,
                                a_pl: float,
                                grav_const: float,
                                au_: float,
                                m_solar: float):
    """
    Docstring

    v_rel = v_kep * sqrt(3 - Tiss)

    """

    if not isinstance(tiss, float):
        raise TypeError
    if not isinstance(m_star, float):
        raise TypeError
    if not isinstance(a_pl, float):
        raise TypeError
    if not isinstance(grav_const, float):
        raise TypeError
    if not isinstance(au_, float):
        raise TypeError
    if not isinstance(m_solar, float):
        raise TypeError

    v_kep = np.sqrt((grav_const * m_star * m_solar) / (a_pl * au_))
    v_rel = v_kep * np.sqrt(3 - tiss)

    return v_rel


def calculate_escape_velocity(m_pl: float,
                              r_pl: float,
                              grav_const: float,
                              au_: float,
                              m_solar: float):
    """
    Docstring
    """
    if not isinstance(m_pl, float):
        raise TypeError
    if not isinstance(r_pl, float):
        raise TypeError
    if not isinstance(grav_const, float):
        raise TypeError
    if not isinstance(au_, float):
        raise TypeError
    if not isinstance(m_solar, float):
        raise TypeError

    v_esc = np.sqrt( (2 * grav_const * m_pl * m_solar) / (r_pl * au_))

    return v_esc


def generate_vimp_dist(tiss_params: np.ndarray,
                       m_star: float,
                       m_pl: float,
                       r_pl: float,
                       a_pl: float,
                       au_: float,
                       grav_const: float,
                       m_solar: float):
    """
    Docstring
    """
    if not isinstance(tiss_params, np.ndarray):
        raise TypeError
    if not isinstance(m_star, float):
        raise TypeError
    if not isinstance(m_pl, float):
        raise TypeError
    if not isinstance(r_pl, float):
        raise TypeError
    if not isinstance(a_pl, float):
        raise TypeError
    if not isinstance(grav_const, float):
        raise TypeError
    if not isinstance(au_, float):
        raise TypeError
    if not isinstance(m_solar, float):
        raise TypeError

    v_esc = calculate_escape_velocity(m_pl=m_pl,
                                      r_pl=r_pl,
                                      grav_const=grav_const,
                                      au_=au_,
                                      m_solar=m_solar)

    v_imp = []

    for tiss in tiss_params:

        v_rel = calculate_relative_velocity(tiss=tiss,
                                            m_star=m_star,
                                            a_pl=a_pl,
                                            grav_const=grav_const,
                                            au_=au_,
                                            m_solar=m_solar)

        v_imp = np.append(v_imp, np.sqrt(v_esc ** 2 + v_rel ** 2))

    return v_imp
