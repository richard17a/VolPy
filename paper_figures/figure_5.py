"""
Docstring
"""

import numpy as np # pylint: disable=import-error
import matplotlib.pyplot as plt # pylint: disable=import-error
import matplotlib # pylint: disable=import-error
from volpy.fig_utils import set_size, read_sim_data

matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'


def main():
    """
    Docstring
    """

    vimp_m, vimp_g = read_sim_data()

    hill_spacings = np.array([50, 30, 20, 10])

    vimp_m10 = vimp_m[0]
    vimp_m20 = vimp_m[1]
    vimp_m30 = vimp_m[2]
    vimp_m50 = vimp_m[3]

    vimp_g10 = vimp_g[0]
    vimp_g20 = vimp_g[1]
    vimp_g30 = vimp_g[2]
    vimp_g50 = vimp_g[3]

    fracs_12m = 100 * np.array([len(vimp_m50[vimp_m50 < 12])/len(vimp_m50),
                                len(vimp_m30[vimp_m30 < 12])/len(vimp_m30),
                                len(vimp_m20[vimp_m20 < 12])/len(vimp_m20),
                                len(vimp_m10[vimp_m10 < 12])/len(vimp_m10)])
    fracs_13m = 100 * np.array([len(vimp_m50[vimp_m50 < 13])/len(vimp_m50),
                                len(vimp_m30[vimp_m30 < 13])/len(vimp_m30),
                                len(vimp_m20[vimp_m20 < 13])/len(vimp_m20),
                                len(vimp_m10[vimp_m10 < 13])/len(vimp_m10)])
    fracs_14m = 100 * np.array([len(vimp_m50[vimp_m50 < 14])/len(vimp_m50),
                                len(vimp_m30[vimp_m30 < 14])/len(vimp_m30),
                                len(vimp_m20[vimp_m20 < 14])/len(vimp_m20),
                                len(vimp_m10[vimp_m10 < 14])/len(vimp_m10)])
    fracs_15m = 100 * np.array([len(vimp_m50[vimp_m50 < 15])/len(vimp_m50),
                                len(vimp_m30[vimp_m30 < 15])/len(vimp_m30),
                                len(vimp_m20[vimp_m20 < 15])/len(vimp_m20),
                                len(vimp_m10[vimp_m10 < 15])/len(vimp_m10)])
    fracs_16m = 100 * np.array([len(vimp_m50[vimp_m50 < 16])/len(vimp_m50),
                                len(vimp_m30[vimp_m30 < 16])/len(vimp_m30),
                                len(vimp_m20[vimp_m20 < 16])/len(vimp_m20),
                                len(vimp_m10[vimp_m10 < 16])/len(vimp_m10)])
    fracs_17m = 100 * np.array([len(vimp_m50[vimp_m50 < 17])/len(vimp_m50),
                                len(vimp_m30[vimp_m30 < 17])/len(vimp_m30),
                                len(vimp_m20[vimp_m20 < 17])/len(vimp_m20),
                                len(vimp_m10[vimp_m10 < 17])/len(vimp_m10)])

    fracs_12g = 100 * np.array([len(vimp_g50[vimp_g50 < 12])/len(vimp_g50),
                                len(vimp_g30[vimp_g30 < 12])/len(vimp_g30),
                                len(vimp_g20[vimp_g20 < 12])/len(vimp_g20),
                                len(vimp_g10[vimp_g10 < 12])/len(vimp_g10)])
    fracs_13g = 100 * np.array([len(vimp_g50[vimp_g50 < 13])/len(vimp_g50),
                                len(vimp_g30[vimp_g30 < 13])/len(vimp_g30),
                                len(vimp_g20[vimp_g20 < 13])/len(vimp_g20),
                                len(vimp_g10[vimp_g10 < 13])/len(vimp_g10)])
    fracs_14g = 100 * np.array([len(vimp_g50[vimp_g50 < 14])/len(vimp_g50),
                                len(vimp_g30[vimp_g30 < 14])/len(vimp_g30),
                                len(vimp_g20[vimp_g20 < 14])/len(vimp_g20),
                                len(vimp_g10[vimp_g10 < 14])/len(vimp_g10)])
    fracs_15g = 100 * np.array([len(vimp_g50[vimp_g50 < 15])/len(vimp_g50),
                                len(vimp_g30[vimp_g30 < 15])/len(vimp_g30),
                                len(vimp_g20[vimp_g20 < 15])/len(vimp_g20),
                                len(vimp_g10[vimp_g10 < 15])/len(vimp_g10)])
    fracs_16g = 100 * np.array([len(vimp_g50[vimp_g50 < 16])/len(vimp_g50),
                                len(vimp_g30[vimp_g30 < 16])/len(vimp_g30),
                                len(vimp_g20[vimp_g20 < 16])/len(vimp_g20),
                                len(vimp_g10[vimp_g10 < 16])/len(vimp_g10)])
    fracs_17g = 100 * np.array([len(vimp_g50[vimp_g50 < 17])/len(vimp_g50),
                                len(vimp_g30[vimp_g30 < 17])/len(vimp_g30),
                                len(vimp_g20[vimp_g20 < 17])/len(vimp_g20),
                                len(vimp_g10[vimp_g10 < 17])/len(vimp_g10)])

    fig_width, fig_height = set_size('thesis', 1, (1, 1))

    fig = plt.figure(figsize=(1.6 * fig_width, 1. * fig_height))

    ax01 = fig.add_subplot(1, 2, 1)
    ax02 = fig.add_subplot(1, 2, 2, sharex = ax01, sharey=ax01)

    ax01.plot(hill_spacings, fracs_12m, marker='.', label=r'$v<12$ km/s')
    ax01.plot(hill_spacings, fracs_13m, marker='x', label=r'$v<13$ km/s')
    ax01.plot(hill_spacings, fracs_14m, marker='+', label=r'$v<14$ km/s')
    ax01.plot(hill_spacings, fracs_15m, marker='d', label=r'$v<15$ km/s', markersize=4)
    ax01.plot(hill_spacings, fracs_16m, marker='s', label=r'$v<16$ km/s', markersize=4)
    ax01.plot(hill_spacings, fracs_17m, marker='*', label=r'$v<17$ km/s')
    ax01.set_ylim(0, 100)
    ax01.set_yticks([0, 20, 40, 60, 80, 100])
    ax01.set_yticklabels([0, 20, 40, 60, 80, 100])
    ax01.tick_params(direction="in")
    ax01.legend(loc='upper right')
    ax01.annotate(r'$M_\ast=0.1 M_\mathrm{Sun}$', xy=(0.05, 0.90), xycoords='axes fraction',
                  bbox={"boxstyle":'round', "fc":'white', "ec":'gainsboro'})
    ax01.text(9, 103, '(a)', fontsize=13)
    ax01.set_xlabel('$\Delta$ [mutual Hill radii]', fontsize=13)

    ax02.plot(hill_spacings, fracs_12g, marker='.', label=r'$v<12$ km/s')
    ax02.plot(hill_spacings, fracs_13g, marker='x', label=r'$v<13$ km/s')
    ax02.plot(hill_spacings, fracs_14g, marker='+', label=r'$v<14$ km/s')
    ax02.plot(hill_spacings, fracs_15g, marker='d', label=r'$v<15$ km/s', markersize=4)
    ax02.plot(hill_spacings, fracs_16g, marker='s', label=r'$v<16$ km/s', markersize=4)
    ax02.plot(hill_spacings, fracs_17g, marker='*', label=r'$v<17$ km/s')
    ax02.annotate(r'$M_\ast=1.0 M_\mathrm{Sun}$', xy=(0.05, 0.90), xycoords='axes fraction',
              bbox={"boxstyle":'round', "fc":'white', "ec":'gainsboro'})
    ax02.minorticks_on()
    ax02.tick_params(direction="in", labelleft=True, which='both')
    ax02.text(9, 103, '(b)', fontsize=13)
    ax02.set_xlabel('$\Delta$ [mutual Hill radii]', fontsize=13)

    fig.text(0.07, 0.5,
        'Fraction of velocities (%)', va='center', rotation='vertical', fontsize=13)

    plt.subplots_adjust(wspace=0.1)

    plt.show()


if __name__ == "__main__":
    main()
