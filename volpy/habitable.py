"""
Docstring
"""

import numpy as np # pylint: disable=import-error
from astropy import constants as const # pylint: disable=import-error
from volpy.luminosity import calc_luminosity


def calculate_effective_flux(mass: np.ndarray,
                             temp_eff: np.ndarray,
                             inner=True):
    """
    Calculate the effective flux for a given array of stellar masses and effective
    temperatures. This follows equation (2) from Kopparpu+2013

    Args:
        mass (np.ndarray): An array of stellar masses.
        temp_eff (np.ndarray): An array of effective temperatures.
        inner (bool): A flag indicating whether to calculate the effective
                      flux for the inner region.

    Returns:
        np.ndarray: The calculated effective flux values.

    Raises:
        TypeError: If mass is not a numpy array.
        ValueError: If the maximum stellar mass exceeds 3 M_sun.
        TypeError: If temp_eff is not a numpy array.
        TypeError: If inner is not a boolean.
    """
    if not isinstance(mass, np.ndarray):
        raise TypeError('Stellar masses must be a numpy array.')
    if np.max(mass) > 3.:
        raise ValueError('Stellar masses cannot exceed 3 M_sun.')
    if not isinstance(temp_eff, np.ndarray):
        raise TypeError('Effective temperatures must be a numpy array.')
    if not isinstance(inner, bool):
        raise TypeError('Boundary flag must be a bool.')

    if inner:
        s_0 = 1.0146
        _a = 8.1884e-5
        _b = 1.9394e-9
        _c = -4.3618e-12
        _d = -6.8260e-16
    else:
        s_0 =  0.3507
        _a = 5.9578e-5
        _b = 1.6707e-9
        _c = -3.0058e-12
        _d = -5.1925e-16

    temp_star = temp_eff - 5780

    flux = []
    flux_low = s_0 + _a * temp_star[mass <=1] + _b * temp_star[mass <=1]**2 +\
               _c * temp_star[mass <=1]**3 + _d * temp_star[mass <=1]**4
    flux = np.append(flux, flux_low)
    flux = np.append(flux, flux_low[-1] * np.ones(len(mass[mass > 1.])))

    return flux


def calculate_habitable_zone(mass: np.ndarray,
                             output_lims=False):
    """
    Calculate the habitable zone for a given array of stellar masses.

    Args:
        mass (np.ndarray): An array of stellar masses.
        output_lims (bool): A flag indicating whether to output the inner
                            and outer limits of the habitable zone.

    Returns:
        np.ndarray: The calculated habitable zone values.

    Raises:
        TypeError: If mass is not a numpy array.
        ValueError: If the maximum stellar mass exceeds 3 M_sun.
        TypeError: If output_lims is not a boolean.
    """
    if not isinstance(mass, np.ndarray):
        raise TypeError('Stellar masses must be a numpy array.')
    if np.max(mass) > 3.:
        raise ValueError('Stellar masses cannot exceed 3 M_sun.')
    if not isinstance(output_lims, bool):
        raise TypeError('Outer snowline must be True or False.')

    r_star = const.R_sun.value * mass ** 0.8

    lum = calc_luminosity(mass=mass)

    temp_eff = ((lum * const.L_sun.value / (4 * np.pi * const.sigma_sb.value)) *\
                ( r_star ) ** (-2.)) ** (1./4.)

    flux_eff_inner = calculate_effective_flux(mass=mass,
                                              temp_eff=temp_eff,
                                              inner=True)
    flux_eff_outer = calculate_effective_flux(mass=mass,
                                              temp_eff=temp_eff,
                                              inner=False)

    habitabale_zone_inner = (lum / flux_eff_inner) ** 0.5
    habitabale_zone_outer = (lum / flux_eff_outer) ** 0.5

    habitable_zone = 0.5 * (habitabale_zone_inner + habitabale_zone_outer)

    if not output_lims:
        return habitable_zone

    return habitable_zone, habitabale_zone_inner, habitabale_zone_outer
