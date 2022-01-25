"""Utilies."""

import matplotlib.pyplot as plt

from settings import PATH

###################################################################################################
###################################################################################################

def save_fig(save, file_name, folder=PATH, **settings):
    """Utility for saving out figures."""

    if save:
        plt.savefig(folder / file_name, bbox_inches='tight')
