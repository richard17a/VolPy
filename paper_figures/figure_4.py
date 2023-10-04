"""
Docstring
"""

import numpy as np # pylint: disable=import-error
import matplotlib.pyplot as plt # pylint: disable=import-error
from matplotlib.lines import Line2D # pylint: disable=import-error
import matplotlib # pylint: disable=import-error
from volpy.fig_utils import set_size, read_sim_data
from volpy.habitable import calculate_habitable_zone
from volpy.planet import Planet
from volpy.star import Star
from volpy.velocities.orbital_elements import calculate_tisserand_hill_spacing
from volpy.velocities.generate_vimp_dist import generate_vimp_dist

matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'


def main():
    """
    Docstring
    """

    mass = np.array([0.1, 0.4, 1])
    habitables = calculate_habitable_zone(mass=mass,
                                          output_lims=True)

    habitable = habitables[0]

    gtype = Star(mass=1.)
    mdwarf_01 = Star(mass=.1)
    mdwarf_04 = Star(mass=.4)

    earth_m_01 = Planet(mass=3.00e-6,
                       radius=4.26e-5,
                       semimajor_axis=habitable[np.argmin(np.abs(np.array(mass)-.1))])
    earth_m_04 = Planet(mass=3.00e-6,
                       radius=4.26e-5,
                       semimajor_axis=habitable[np.argmin(np.abs(np.array(mass)-.4))])
    earth_g = Planet(mass=3.00e-6,
                     radius=4.26e-5,
                     semimajor_axis=habitable[np.argmin(np.abs(np.array(mass)-1.))])

    hill_spacings = np.array([10, 30, 50])

    tiss_spacing_m_01, tiss_spacing_m_04, tiss_spacing_g = [], [], []

    for num in hill_spacings:
        tiss_spacing_m_01 = np.append(
            tiss_spacing_m_01,
            calculate_tisserand_hill_spacing(
                habitable_zone=habitable[0],
                planet=earth_m_01,
                star=mdwarf_01,
                delta_planet=num)
            )
        tiss_spacing_m_04 = np.append(
            tiss_spacing_m_04,
            calculate_tisserand_hill_spacing(
                habitable_zone=habitable[0],
                planet=earth_m_04,
                star=mdwarf_04,
                delta_planet=num)
            )
        tiss_spacing_g = np.append(
            tiss_spacing_g,
            calculate_tisserand_hill_spacing(
                habitable_zone=habitable[1],
                planet=earth_g,
                star=gtype,
                delta_planet=num)
            )

    vimp_m_theory_01 = generate_vimp_dist(tiss_params=tiss_spacing_m_01,
                                         star=mdwarf_01,
                                         planet=earth_m_01)
    vimp_m_theory_04 = generate_vimp_dist(tiss_params=tiss_spacing_m_04,
                                         star=mdwarf_04,
                                         planet=earth_m_04)

    vimp_m_01, vimp_m_04, vimp_g = read_sim_data()


    fig_width, fig_height = set_size('thesis', 1, (1, 1))

    fig = plt.figure(figsize=(1.3 * fig_width, 1. * fig_height))

    line_1 = Line2D([0,1], [0,1], linestyle='-', color='#377eb8')
    line_2 = Line2D([0,1], [0,1], linestyle='-', color='#ff7f00')
    line_3 = Line2D([0,1], [0,1], linestyle='-', color='#a65628')

    ax01 = fig.add_subplot(1, 2, 1)
    ax02 = fig.add_subplot(1, 2, 2, sharex = ax01, sharey = ax01)

    ax01.hist(vimp_g[3], density=True, bins=50, alpha=0.3, color='tab:gray')
    ax01.hist(vimp_m_01[3], density=True, bins=60, histtype='step', color='#377eb8')
    ax01.hist(vimp_m_01[2], density=True, bins=60, histtype='step', color='#ff7f00')
    ax01.hist(vimp_m_01[0], density=True, bins=60, histtype='step', color='#a65628')

    ax01.axvline(vimp_m_theory_01[2] / 1e3, ls='--', c='#377eb8')
    ax01.axvline(vimp_m_theory_01[1] / 1e3, ls='--', c='#ff7f00')
    ax01.axvline(vimp_m_theory_01[0] / 1e3, ls='--', c='#a65628')

    ax01.legend([line_1, line_2, line_3],
               [r'$\Delta a = 50 R_{H,m}$', r'$\Delta a = 30 R_{H,m}$',
                r'$\Delta a = 10 R_{H,m}$'], borderpad=0.5)

    ax01.set_xlim(10, 40)
    ax01.set_ylim(0, 0.25)

    ax01.set_xlabel('Impact velocity [km/s]', fontsize=13)
    ax01.set_ylabel('Frequency', fontsize=13)

    ax01.text(10, 0.26, '(a)', fontsize=13)
    ax01.annotate(r'$M_\ast=0.1\,M_{\rm Sun}$', xy=(0.05, 0.9), xycoords='axes fraction',
                  bbox={'boxstyle':'round', 'fc':'white', 'ec':'gainsboro'})

    ax01.minorticks_on()
    ax01.tick_params(direction="in", which='both', labelleft=True)

    ax02.hist(vimp_g[3], density=True, bins=50, alpha=0.3, color='tab:gray')
    ax02.hist(vimp_m_04[2], density=True, bins=60, histtype='step', color='#377eb8')
    ax02.hist(vimp_m_04[1], density=True, bins=60, histtype='step', color='#ff7f00')
    ax02.hist(vimp_m_04[0], density=True, bins=60, histtype='step', color='#a65628')

    ax02.axvline(vimp_m_theory_04[2] / 1e3, ls='--', c='#377eb8')
    ax02.axvline(vimp_m_theory_04[1] / 1e3, ls='--', c='#ff7f00')
    ax02.axvline(vimp_m_theory_04[0] / 1e3, ls='--', c='#a65628')

    ax02.legend([line_1, line_2, line_3],
               [r'$\Delta a = 50 R_{H,m}$', r'$\Delta a = 30 R_{H,m}$',
                r'$\Delta a = 10 R_{H,m}$'], borderpad=0.5)

    ax02.set_xlim(10, 40)
    ax02.set_xlabel('Impact velocity [km/s]', fontsize=13)

    ax02.minorticks_on()
    ax02.tick_params(direction="in", which='both', labelleft=False)

    ax02.text(10, 0.26, '(b)', fontsize=13)
    ax02.annotate(r'$M_\ast=0.4\,M_{\rm Sun}$', xy=(0.05, 0.9), xycoords='axes fraction',
                  bbox={'boxstyle':'round', 'fc':'white', 'ec':'gainsboro'})

    plt.subplots_adjust(wspace=0.1)

    plt.show()


if __name__ == "__main__":
    main()
