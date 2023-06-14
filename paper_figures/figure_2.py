"""
Docstring
"""

import numpy as np # pylint: disable=import-error
import matplotlib.pyplot as plt # pylint: disable=import-error
import matplotlib # pylint: disable=import-error
from volpy.habitable import calculate_habitable_zone
from volpy.snowline import calculate_snowline
from volpy.planet import Planet
from volpy.star import Star
from volpy.velocities.orbital_elements import (calculate_eccentricity,
                                               calculate_tisserand,
                                               calculate_tisserand_hill_spacing)
from volpy.velocities.generate_vimp_dist import generate_vimp_dist
from volpy.fig_utils import set_size

matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'


def calculate_mutual_hill_radius(mu_a: float,
                                 mu_b: float,
                                 a_a: float,
                                 a_b: float):
    """
    Calculated the mutual Hill radius for two bodies with
    reduced masses mu_i and semi-major axes a_i.

    R_Hm = 0.5 * ( (mu_i + mu_{i+1}) / 3) ** (1/3) * (a_i + a_{i+1})

    """

    reduced_mass = ( (mu_a + mu_b) / 3) ** (1./3.) / 2

    hill_radius = reduced_mass * (a_a + a_b)

    return hill_radius


def calculate_max_tiss(mu_a: float,
                       mu_b: float,
                       delta: float):
    """
    Docstring
    """

    reduced_mass = ( (mu_a + mu_b) / 3) ** (1./3.) / 2

    tiss = (1 - delta * reduced_mass) + 2 * np.sqrt( 1 + delta * reduced_mass )

    return tiss


def solarsystem_delta_tiss():
    """
    Docstring
    """

    rad_mars_earth = calculate_mutual_hill_radius(mu_a=3.213e-7, mu_b=3.00e-6,
                                                a_a=1.524, a_b=1.)
    rad_earth_venus = calculate_mutual_hill_radius(mu_a=3.00e-6, mu_b=0.815 * 3.00e-6,
                                                 a_a=1., a_b=0.723)
    rad_venus_mercury = calculate_mutual_hill_radius(mu_a=0.815 * 3.00e-6, mu_b=0.055 * 3.00e-6,
                                                   a_a=0.723, a_b=0.387)

    delta_mars_earth = (1.524 - 1.) / rad_mars_earth
    delta_earth_venus = (1. - 0.723) / rad_earth_venus
    delta_venus_mercury = (0.723 - 0.387) / rad_venus_mercury

    tiss_mars_earth = calculate_max_tiss(mu_a=3.213e-7, mu_b=3.00e-6,
                                         delta=delta_mars_earth)
    tiss_earth_venus = calculate_max_tiss(mu_a=3.00e-6, mu_b=0.815*3.00e-6,
                                          delta=delta_earth_venus)
    tiss_venus_mercury = calculate_max_tiss(mu_a=0.815*3.00e-6, mu_b=0.055*3.00e-6,
                                          delta=delta_venus_mercury)

    delta = [delta_mars_earth, delta_earth_venus, delta_venus_mercury]
    tiss = [tiss_mars_earth, tiss_earth_venus, tiss_venus_mercury]

    return delta, tiss


def trappist1_delta_tiss():
    """
    Docstring
    """

    rad_trappist_de = calculate_mutual_hill_radius(mu_a=1.534e-5, mu_b=2.319e-5,
                                                   a_a=21.44e-3, a_b=28.17e-3)
    rad_trappist_ef = calculate_mutual_hill_radius(mu_a=2.319e-5, mu_b=2.544e-5,
                                                   a_a=28.17e-3, a_b=37.10e-3)
    rad_trappist_fg = calculate_mutual_hill_radius(mu_a=2.544e-5, mu_b=5.012e-5,
                                                   a_a=37.10e-3, a_b=45.10e-3)
    rad_trappist_gh = calculate_mutual_hill_radius(mu_a=5.012e-5, mu_b=1.534e-5,
                                                   a_a=45.10e-3, a_b=59.60e-3)

    delta_trappist_de = (28.17 - 21.44) * 1e-3 / rad_trappist_de
    delta_trappist_ef = (37.10 - 28.17) * 1e-3 / rad_trappist_ef
    delta_trappist_fg = (45.10 - 37.10) * 1e-3 / rad_trappist_fg
    delta_trappist_gh = (45.10 - 37.10) * 1e-3 / rad_trappist_gh

    tiss_trappist_de = calculate_max_tiss(mu_a=1.534e-5, mu_b=2.319e-5,
                                          delta=delta_trappist_de)
    tiss_trappist_ef = calculate_max_tiss(mu_a=2.319e-5, mu_b=2.544e-5,
                                          delta=delta_trappist_ef)
    tiss_trappist_fg = calculate_max_tiss(mu_a=2.544e-5, mu_b=5.012e-5,
                                          delta=delta_trappist_fg)
    tiss_trappist_gh = calculate_max_tiss(mu_a=5.012e-5, mu_b=1.534e-5,
                                          delta=delta_trappist_gh)

    delta = [delta_trappist_de, delta_trappist_ef, delta_trappist_fg, delta_trappist_gh]
    tiss = [tiss_trappist_de, tiss_trappist_ef, tiss_trappist_fg, tiss_trappist_gh]

    return delta, tiss


def main():
    """
    Docstring
    """

    fig_width, fig_height = set_size(5.316, 1, (1, 1))
    # fig_width, fig_height = set_size('thesis', 1, (1, 1))

    mass = np.logspace(-1, 0, 1000)
    habitables = calculate_habitable_zone(mass=mass,
                                          output_lims=True)
    snowlines = calculate_snowline(mass=mass,
                                   output_lims=True)

    habitable = habitables[0]
    snowline =snowlines[0]

    gtype = Star(mass=1.)
    ktype = Star(mass=.7)
    mdwarf01 = Star(mass=.1)
    mdwarf04 = Star(mass=.4)
    earth_m01 = Planet(mass=3.00e-6,
                       radius=4.26e-5,
                       semimajor_axis=habitable[np.argmin(np.abs(np.array(mass)-.1))])
    earth_g = Planet(mass=3.00e-6,
                     radius=4.26e-5,
                     semimajor_axis=habitable[np.argmin(np.abs(np.array(mass)-1.))])
    earth_k = Planet(mass=3.00e-6,
                     radius=4.26e-5,
                     semimajor_axis=habitable[np.argmin(np.abs(np.array(mass)-.7))])
    earth_m04 = Planet(mass=3.00e-6,
                       radius=4.26e-5,
                       semimajor_axis=habitable[np.argmin(np.abs(np.array(mass)-.4))])

    num_planets = np.linspace(1, 7, 7)

    delta_crit = 2 * np.sqrt(3) / (1 + np.sqrt(3) *\
                (2 * earth_g.mass / 3 / gtype.mass) ** (1./3.))

    hill_spacings = np.linspace(delta_crit, 80, 10000)

    ecc_m, ecc_g = [], []
    tiss_m, tiss_g = [], []
    tiss_spacing_m01, tiss_spacing_g, tiss_spacing_m04, tiss_spacing_k = [], [], [], []

    for num in num_planets:

        ecc_m = np.append(ecc_m, calculate_eccentricity(habitable_zone=habitable[0],
                                                        snow_line=snowline[0],
                                                        num_planets=int(num)))
        ecc_g = np.append(ecc_g, calculate_eccentricity(habitable_zone=habitable[-1],
                                                        snow_line=snowline[-1],
                                                        num_planets=int(num)))

        tiss_m = np.append(tiss_m, calculate_tisserand(habitable_zone=habitable[0],
                                                       snow_line=snowline[0],
                                                       num_planets=int(num)))
        tiss_g = np.append(tiss_g, calculate_tisserand(habitable_zone=habitable[-1],
                                                       snow_line=snowline[-1],
                                                       num_planets=int(num)))

    for num in hill_spacings:
        tiss_spacing_m01 = np.append(
            tiss_spacing_m01,
            calculate_tisserand_hill_spacing(
                habitable_zone=habitable[np.argmin(np.abs(np.array(mass)-.1))],
                planet=earth_m01,
                star=mdwarf01,
                delta_planet=num)
            )
        tiss_spacing_g = np.append(
            tiss_spacing_g,
            calculate_tisserand_hill_spacing(
                habitable_zone=habitable[np.argmin(np.abs(np.array(mass)-1.))],
                planet=earth_g,
                star=gtype,
                delta_planet=num)
            )
        tiss_spacing_k = np.append(
            tiss_spacing_k,
            calculate_tisserand_hill_spacing(
                habitable_zone=habitable[np.argmin(np.abs(np.array(mass)-.7))],
                planet=earth_k,
                star=ktype,
                delta_planet=num)
            )
        tiss_spacing_m04 = np.append(
            tiss_spacing_m04,
            calculate_tisserand_hill_spacing(
                habitable_zone=habitable[np.argmin(np.abs(np.array(mass)-.4))],
                planet=earth_m04,
                star=mdwarf04,
                delta_planet=num)
            )

    delta_solar_system, tiss_solar_system = solarsystem_delta_tiss()
    delta_trappist, tiss_trappist = trappist1_delta_tiss()

    v_esc = earth_m01.calculate_escape_velocity()

    v_imp_spacing_g = generate_vimp_dist(tiss_params=tiss_spacing_g,
                                         star=gtype,
                                         planet=earth_g)
    v_imp_spacing_k = generate_vimp_dist(tiss_params=tiss_spacing_k,
                                         star=ktype,
                                         planet=earth_k)
    v_imp_spacing_m01 = generate_vimp_dist(tiss_params=tiss_spacing_m01,
                                           star=mdwarf01,
                                           planet=earth_m01)
    v_imp_spacing_m04 = generate_vimp_dist(tiss_params=tiss_spacing_m04,
                                           star=mdwarf04,
                                           planet=earth_m04)

    fig = plt.figure(figsize=(1.6 * fig_width, 1. * fig_height))
    ax01 = fig.add_subplot(1, 2, 1)
    ax02 = fig.add_subplot(1, 2, 2, sharex = ax01)

    ax01.axhline(3., ls='--', c='tab:gray', xmin=delta_crit/max(hill_spacings))
    ax01.plot(hill_spacings, tiss_spacing_g, label=r'1.0 $M_\mathrm{Sun}$', c='#a65628')
    ax01.plot(hill_spacings, tiss_spacing_k, label=r'0.7 $M_\mathrm{Sun}$', c='#4daf4a')
    ax01.plot(hill_spacings, tiss_spacing_m04, label=r'0.4 $M_\mathrm{Sun}$', c='#ff7f00')
    ax01.plot(hill_spacings, tiss_spacing_m01, label=r'0.1 $M_\mathrm{Sun}$', c='#377eb8')
    ax01.plot(delta_solar_system, tiss_solar_system, '.', c='dimgray')
    ax01.plot(delta_trappist, tiss_trappist, 'x', c='dimgray')
    ax01.text(42.7, 2.983, r'Solar System',
             rotation=-6, color='tab:gray')
    ax01.text(4.2, 2.97, r'TRAPPIST-1',
             rotation=-15, color='tab:gray', fontsize=9)
    ax01.axvspan(0, delta_crit, alpha=0.5, color='tab:gray')
    ax01.text(delta_crit / 4, 2.885, 'Unstable', rotation=90)
    ax01.set_ylabel(r'$\mathcal{T}_\mathrm{max}$', fontsize=13)
    ax01.set_xlabel(r'$\Delta$ [mutual Hill radii]', fontsize=13)
    ax01.set_xlim(0, 80)
    ax01.legend(loc=(0.08, 0.045), borderpad=0.5)
    ax01.text(0.5, 3.015, '(a)', fontsize=13)
    ax01.minorticks_on()
    ax01.tick_params(direction='in', which='both')
    ax01.set_yticks([2.8, 2.85, 2.9, 2.95, 3.])

    ax02.axvspan(0, delta_crit, alpha=0.5, color='tab:gray')
    ax02.text(delta_crit / 4, 15.725, 'Unstable', rotation=90)
    ax02.text(5, 14.3, 'efficient organic delivery', color='tab:gray')
    ax02.text(5, 20.2, 'inefficient organic delivery', color='tab:gray')
    ax02.axhline(v_esc / 1e3, ls='--', c='tab:gray', xmin=delta_crit/max(hill_spacings))
    ax02.axhline(15., ls=':', c='tab:gray', alpha=0.5, xmin=delta_crit/max(hill_spacings))
    ax02.axhline(20., ls='-.', c='tab:gray', alpha=0.5, xmin=delta_crit/max(hill_spacings))
    ax02.plot(hill_spacings, v_imp_spacing_g / 1e3, label=r'1.0 $M_\mathrm{Sun}$', c='#a65628')
    ax02.plot(hill_spacings, v_imp_spacing_k / 1e3, label=r'0.7 $M_\mathrm{Sun}$', c='#4daf4a')
    ax02.plot(hill_spacings, v_imp_spacing_m04 / 1e3, label=r'0.4 $M_\mathrm{Sun}$', c='#ff7f00')
    ax02.plot(hill_spacings, v_imp_spacing_m01 / 1e3, label=r'0.1 $M_\mathrm{Sun}$', c='#377eb8')

    ax02.set_ylabel(r'$v_\mathrm{imp}$ [km/s]', fontsize=13)
    ax02.set_xlabel(r'$\Delta$ [mutual Hill radii]', fontsize=13)
    ax02.set_ylim(11, )
    ax02.set_xlim(0, 80)
    ax02.text(1.05, 22.3, '(b)', fontsize=13)
    ax02.minorticks_on()
    ax02.tick_params(direction='in', which='both')

    # plt.savefig('Tiss_vimp_hill_spacing.pdf', format='pdf', bbox_inches='tight', pad_inches=0.0)

    plt.show()


if __name__ == "__main__":
    main()
