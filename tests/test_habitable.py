"""
Docstring
"""

import pytest # pylint: disable=import-error
import numpy as np # pylint: disable=import-error
from astropy import constants as const # pylint: disable=import-error
from volpy.habitable import calculate_effective_flux, calculate_habitable_zone
from volpy.luminosity import calc_luminosity
from volpy.snowline import calculate_snowline


def test_calculate_effective_flux():
    """
    Docstring
    """

    mass = np.logspace(-1, np.log10(3), 1000)
    r_star = const.R_sun.value * mass ** 0.8

    lum = calc_luminosity(mass=mass)

    temp_eff = ((lum * const.L_sun.value / (4 * np.pi * const.sigma_sb.value)) *\
                ( r_star ) ** (-2.)) ** (1./4.)

    flux_eff_in = calculate_effective_flux(mass=mass,
                                           temp_eff=temp_eff)
    flux_eff_out = calculate_effective_flux(mass=mass,
                                            temp_eff=temp_eff,
                                            inner=False)

    with pytest.raises(TypeError):
        calculate_effective_flux(mass=mass,
                                 temp_eff=temp_eff,
                                 inner='true')

    assert len(flux_eff_in) == len(mass)
    assert len(flux_eff_in) == len(flux_eff_out)
    assert (flux_eff_in > flux_eff_out).all


def test_calculate_habitable_zone():
    """
    Docstring
    """

    mass = np.logspace(-1, np.log10(3), 1000)
    habitable, habitable_in, habitable_out = calculate_habitable_zone(mass=mass,
                                                                      output_lims=True)
    snowline = calculate_snowline(mass=mass)

    assert len(habitable) == len(mass)
    assert len(habitable_out) == len(habitable)
    assert len(habitable_out) == len(habitable_in)
    assert (habitable_out > habitable_in).all
    assert (habitable > snowline).all
