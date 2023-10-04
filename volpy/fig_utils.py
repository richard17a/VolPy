"""
Docstring
"""
import numpy as np # pylint: disable=import-error


def set_size(width, fraction=1, subplots=(1, 1)):
    """
    Set figure dimensions to avoid scaling in LaTeX.
    This code is from: https://jwalton.info/Embed-Publication-Matplotlib-Latex/

    Parameters
    ----------
    width: float or string
            Document width in points, or string of predined document type
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    subplots: array-like, optional
            The number of rows and columns of subplots.
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    if width == 'thesis':
        width_pt = 426.79135
        width_pt = width_pt / 72.27
    elif width == 'beamer':
        width_pt = 307.28987
        width_pt = width_pt / 72.27
    else:
        width_pt = width

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    golden_ratio = (5**.5 - 1) / 2


    fig_width_in = width_pt * fraction
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    return (fig_width_in, fig_height_in)


def read_sim_data(flag=0):
    """
    Read simulation data from files.

    Returns:
        vimp_m_01 (tuple): Velocity data for 0.1 M_Sun M-type dwarf simulations
        vimp_m_04 (tuple): Velocity data for 0.4 M_Sun M-type dwarf simulations
        vimp_g (tuple): Velocity data for G-type dwarf simulations
    """

    vals_m_01_10 = np.loadtxt('../rebound_scripts/data_files/M01dwarf_delta10.txt', unpack=True)
    vals_m_01_20 = np.loadtxt('../rebound_scripts/data_files/M01dwarf_delta20.txt', unpack=True)
    vals_m_01_30 = np.loadtxt('../rebound_scripts/data_files/M01dwarf_delta30.txt', unpack=True)
    vals_m_01_50 = np.loadtxt('../rebound_scripts/data_files/M01dwarf_delta50.txt', unpack=True)

    # Unit convertion into km/s
    vimp_m_01_10 = 29.805655 * vals_m_01_10[1]
    vimp_m_01_20 = 29.805655 * vals_m_01_20[1]
    vimp_m_01_30 = 29.805655 * vals_m_01_30[1]
    vimp_m_01_50 = 29.805655 * vals_m_01_50[1]

    vimp_m_01 = (vimp_m_01_10, vimp_m_01_20, vimp_m_01_30, vimp_m_01_50)

    vals_m_04_10 = np.loadtxt('../rebound_scripts/data_files/M04dwarf_delta10.txt', unpack=True)
    vals_m_04_30 = np.loadtxt('../rebound_scripts/data_files/M04dwarf_delta30.txt', unpack=True)
    vals_m_04_50 = np.loadtxt('../rebound_scripts/data_files/M04dwarf_delta50.txt', unpack=True)

    # Unit convertion into km/s
    vimp_m_04_10 = 29.805655 * vals_m_04_10[1]
    vimp_m_04_30 = 29.805655 * vals_m_04_30[1]
    vimp_m_04_50 = 29.805655 * vals_m_04_50[1]

    vimp_m_04 = (vimp_m_04_10, vimp_m_04_30, vimp_m_04_50)

    vals_g10 = np.loadtxt('../rebound_scripts/data_files/Gtype_delta10.txt', unpack=True)
    vals_g20 = np.loadtxt('../rebound_scripts/data_files/Gtype_delta20.txt', unpack=True)
    vals_g30 = np.loadtxt('../rebound_scripts/data_files/Gtype_delta30.txt', unpack=True)
    vals_g50 = np.loadtxt('../rebound_scripts/data_files/Gtype_delta50.txt', unpack=True)

    # Unit convertion into km/s
    vimp_g10 = 29.805655 * vals_g10[1]
    vimp_g20 = 29.805655 * vals_g20[1]
    vimp_g30 = 29.805655 * vals_g30[1]
    vimp_g50 = 29.805655 * vals_g50[1]

    vimp_g = (vimp_g10, vimp_g20, vimp_g30, vimp_g50)

    if flag == 0:
        return vimp_m_01, vimp_m_04, vimp_g
    elif flag == 1:
        return vimp_m_01, vimp_g
