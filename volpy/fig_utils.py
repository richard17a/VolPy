"""
Docstring
"""
import numpy as np # pylint: disable=import-error


def set_size(width, fraction=1, subplots=(1, 1)):
    """Set figure dimensions to avoid scaling in LaTeX.

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


def read_sim_data():
    """
    Docstring
    """

    vals_m10 = np.loadtxt('../rebound_scripts/data_files/Mdwarf_delta10.txt', unpack=True)
    vals_m20 = np.loadtxt('../rebound_scripts/data_files/Mdwarf_delta20.txt', unpack=True)
    vals_m30 = np.loadtxt('../rebound_scripts/data_files/Mdwarf_delta30.txt', unpack=True)
    vals_m50 = np.loadtxt('../rebound_scripts/data_files/Mdwarf_delta50.txt', unpack=True)

    # Unit convertion into km/s
    vimp_m10 = 29.805655 * vals_m10[1]
    vimp_m20 = 29.805655 * vals_m20[1]
    vimp_m30 = 29.805655 * vals_m30[1]
    vimp_m50 = 29.805655 * vals_m50[1]

    vimp_m = (vimp_m10, vimp_m20, vimp_m30, vimp_m50)

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

    return vimp_m, vimp_g
