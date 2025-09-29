# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 13:05:53 2025

@author: ravra
"""
import numpy as np
def generate_sine_wave(frequency, duration, sample_rate):
    """
    generates a sine wave

    Parameters
    ----------
    frequency : .
    duration : how long the sine wave continues for.
    sample_rate : TYPE
        DESCRIPTION.

    Returns
    -------
    y : TYPE
        DESCRIPTION.

    """
    t = np.linspace(0, duration, sample_rate)
    y = np.sin(frequency*2*np.pi*t)
    return y

def u(start, finish, delay, amplitude):
    t = np.linspace(start, finish, 1000)
    return np.where(t<0 - delay, 0, amplitude)
