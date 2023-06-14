"""
Docstring
"""

import numpy as np # pylint: disable=import-error
import matplotlib.pyplot as plt # pylint: disable=import-error
import matplotlib # pylint: disable=import-error
from mpl_toolkits.axes_grid1 import make_axes_locatable # pylint: disable=import-error
from volpy.fig_utils import set_size
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

    fig_width, fig_height = set_size('thesis', 1, (1, 1))

    masses = np.logspace(np.log10(0.095), np.log10(2.1), 200)
    habitables = calculate_habitable_zone(mass=masses,
                                          output_lims=True)

    habitable = habitables[0]

    planet_spacings = np.linspace(5, 80, 200)

    m_grid, ps_grid = np.meshgrid(masses, planet_spacings)

    vimp_05 = np.zeros_like(ps_grid)
    vimp_1 = np.zeros_like(ps_grid)
    vimp_2 = np.zeros_like(ps_grid)

    for i, mass in enumerate(masses):

        for j, delta in enumerate(planet_spacings):

            star = Star(mass=masses[i])
            planet_05 = Planet(mass=0.5 * 3.00e-6,
                              radius=4.26e-5,
                              semimajor_axis=habitable[np.argmin(np.abs(np.array(masses)-mass))])
            planet_1 = Planet(mass=3.00e-6,
                              radius=4.26e-5,
                              semimajor_axis=habitable[np.argmin(np.abs(np.array(masses)-mass))])
            planet_2 = Planet(mass=2. * 3.00e-6,
                               radius=4.26e-5,
                               semimajor_axis=habitable[np.argmin(np.abs(np.array(masses)-mass))])

            tiss_05 = calculate_tisserand_hill_spacing(
                    habitable_zone=habitable[np.argmin(np.abs(np.array(masses)-mass))],
                    planet=planet_05,
                    star=star,
                    delta_planet=np.array([delta]))
            tiss_1 = calculate_tisserand_hill_spacing(
                    habitable_zone=habitable[np.argmin(np.abs(np.array(masses)-mass))],
                    planet=planet_1,
                    star=star,
                    delta_planet=np.array([delta]))
            tiss_2 = calculate_tisserand_hill_spacing(
                    habitable_zone=habitable[np.argmin(np.abs(np.array(masses)-mass))],
                    planet=planet_2,
                    star=star,
                    delta_planet=np.array([delta]))

            v_imp_05 = generate_vimp_dist(tiss_params=tiss_05,
                                         star=star,
                                         planet=planet_05)
            v_imp_1 = generate_vimp_dist(tiss_params=tiss_1,
                                         star=star,
                                         planet=planet_1)
            v_imp_2 = generate_vimp_dist(tiss_params=tiss_2,
                                          star=star,
                                          planet=planet_2)

            vimp_05[j,i] =  v_imp_05
            vimp_1[j,i] =  v_imp_1
            vimp_2[j,i] = v_imp_2

    fig = plt.figure(figsize=(1.6 * fig_width, 1. * fig_height))
    ax01 = fig.add_subplot(1, 3, 1)
    ax02 = fig.add_subplot(1, 3, 2, sharex = ax01)
    ax03 = fig.add_subplot(1, 3, 3, sharex = ax01)

    levels = np.linspace(5, 25, 40).round(1)

    ax01.contourf(m_grid, ps_grid, vimp_05 / 1e3, levels=levels, extend='max', cmap='seismic')
    ax01.contour(m_grid, ps_grid, vimp_05 / 1e3, [15],
                linestyles=['--'], colors=['crimson'], linewidths=[0.9])
    ax01.contour(m_grid, ps_grid, vimp_05 / 1e3, [20],
                linestyles=['--'], colors=['k'], linewidths=[0.9])

    ax01.minorticks_on()
    ax01.tick_params(direction='in', which='both')
    ax01.set_xlabel(r'$M_\ast$ [$M_\mathrm{Sun}$]', fontsize=13)

    ax01.set_ylabel(r'$\Delta$ [mutual Hill radii]', fontsize=13)
    ax01.text(0.09, 83, '(a)', fontsize=13)
    ax01.annotate("$M_{\mathrm{pl}} = 0.5 M_{\mathrm{Earth}}$\n$v_{\mathrm{esc}}$ = 7.90 km/s",
                  xy=(0.05,0.075), xycoords='axes fraction',
                  bbox={"boxstyle":"round", "fc":'whitesmoke', "ec":"lightgray"})
    ax01.text(0.106, 65, r'$15~$km/s', color='crimson', rotation=55)
    ax01.text(0.95, 9, 'Efficient\ndelivery', color='white', rotation=0)

    im02 = ax02.contourf(m_grid, ps_grid, vimp_1 / 1e3,
                        levels=levels, extend='max', cmap='seismic')
    ax02.contour(m_grid, ps_grid, vimp_1 / 1e3, [15],
                linestyles=['--'], colors=['crimson'], linewidths=[0.9])
    ax02.contour(m_grid, ps_grid, vimp_1 / 1e3, [20],
                linestyles=['--'], colors=['k'], linewidths=[0.9])

    ax02.set_xscale('log')
    ax02.set_xticks([0.1, 1, 2], [0.1, 1, 2], minor=False)
    ax02.set_yticks([], [], minor=False)
    ax02.set_xlabel(r'$M_\ast$ [$M_\mathrm{Sun}$]', fontsize=13)

    ax02.minorticks_on()
    ax02.tick_params(direction='in', which='both')

    ax02.annotate("$M_{\mathrm{pl}} = M_{\mathrm{Earth}}$\n$v_{\mathrm{esc}}$ = 11.18 km/s",
                  xy=(0.05,0.075), xycoords='axes fraction',
                  bbox={"boxstyle":"round",
                  "fc":'whitesmoke', "ec":"lightgray"})
    ax02.text(0.09, 83, '(b)', fontsize=13)

    ax03.contourf(m_grid, ps_grid, vimp_2 / 1e3, levels=levels, extend='max', cmap='seismic')
    ax03.contour(m_grid, ps_grid, vimp_2 / 1e3, [15], linestyles=['--'], colors=['crimson'])
    ax03.contour(m_grid, ps_grid, vimp_2 / 1e3, [20], linestyles=['--'], colors=['k'],
                linewidths=[0.9])

    ax03.minorticks_on()
    ax03.tick_params(direction='in', which='both')
    ax03.set_yticks([], [], minor=False)

    divider = make_axes_locatable(ax03)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    cbar = fig.colorbar(im02, cax=cax, orientation='vertical')
    cbar.set_label(r'$v_\mathrm{imp}$ [km/s]', fontsize=13)

    ax03.set_xlabel(r'$M_\ast$ [$M_\mathrm{Sun}$]', fontsize=13)

    ax03.text(0.1, 45, r'$20~$km/s', color='k', rotation=36)
    ax03.text(0.1, 70, 'Inefficient\ndelivery', color='white', rotation=0)
    ax03.text(0.09, 83, '(c)', fontsize=13)

    ax03.annotate("$M_{\mathrm{pl}} = 2M_{\mathrm{Earth}}$\n$v_{\mathrm{esc}}$ = 15.81 km/s",
                  xy=(0.05,0.075), xycoords='axes fraction',
                  bbox={"boxstyle":"round", "fc":'whitesmoke', "ec":"lightgray"})

    plt.subplots_adjust(wspace=0.05)

    fig.savefig('vimp_contours.pdf', format='pdf', bbox_inches='tight',
                pad_inches=0., transparent=True)

    plt.show()


if __name__ == "__main__":
    main()
