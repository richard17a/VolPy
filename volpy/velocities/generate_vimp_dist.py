"""
Docstring
"""

import numpy as np 


def calculate_relative_velocity(tiss: float,
                                M_star: float, 
                                a_pl: float, 
                                G: float, 
                                AU: float, 
                                M_solar: float):
    """
    Docstring

    v_rel = v_kep * sqrt(3 - Tiss)

    """

    if not isinstance(tiss, float):
        raise TypeError
    if not isinstance(M_star, float):
        raise TypeError
    if not isinstance(a_pl, float):
        raise TypeError
    if not isinstance(G, float):
        raise TypeError
    if not isinstance(AU, float):
        raise TypeError
    if not isinstance(M_solar, float):
        raise TypeError

    v_kep = np.sqrt((G * M_star * M_solar) / (a_pl * AU))
    v_rel = v_kep * np.sqrt(3 - tiss)

    return v_rel


def calculate_escape_velocity(M_pl: float, 
                              R_pl: float,
                              G: float,
                              AU: float, 
                              M_solar: float):
    """
    Docstring
    """
    if not isinstance(M_pl, float):
        raise TypeError
    if not isinstance(R_pl, float):
        raise TypeError
    if not isinstance(AU, float):
        raise TypeError
    if not isinstance(M_solar, float):
        raise TypeError

    v_esc = np.sqrt( (2 * G * M_pl * M_solar) / (R_pl * AU))

    return v_esc


def generate_vimp_dist(tiss_params: np.ndarray,
                       M_star: float, 
                       M_pl: float, 
                       R_pl: float, 
                       a_pl: float, 
                       AU: float,
                       G: float,
                       M_solar: float):
    """
    Docstring
    """
    if not isinstance(tiss_params, np.ndarray):
        raise TypeError
    if not isinstance(M_star, float):
        raise TypeError
    if not isinstance(M_pl, float):
        raise TypeError
    if not isinstance(R_pl, float):
        raise TypeError
    if not isinstance(a_pl, float):
        raise TypeError
    if not isinstance(G, float):
        raise TypeError
    if not isinstance(AU, float):
        raise TypeError
    if not isinstance(M_solar, float):
        raise TypeError

    v_esc = calculate_escape_velocity(M_pl=M_pl,
                                      R_pl=R_pl,
                                      G=G,
                                      AU=AU,
                                      M_solar=M_solar)

    v_imp = []

    for tiss in tiss_params:

        v_rel = calculate_relative_velocity(tiss=tiss,
                                            M_star=M_star,
                                            a_pl=a_pl,
                                            G=G,
                                            AU=AU,
                                            M_solar=M_solar)

        v_imp = np.append(v_imp, np.sqrt(v_esc ** 2 + v_rel ** 2))

    return v_imp
