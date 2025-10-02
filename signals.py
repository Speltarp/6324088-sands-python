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
    frequency : Float.
    Number of cycli the wave does per second, measured in Hertz
    duration : Float.
    How long the sine wave continues for.
    sample_rate : Float.
    Amount of plotted points per second.

    Returns
    -------
    y : Float.
    Amplitude
    t : Float.
    Time

    """
    t = np.linspace(0, duration, sample_rate)
    y = np.sin(frequency*2*np.pi*t)
    return t, y

def u(start, finish, amplitude, sample_rate):
    t = np.linspace(start, finish, sample_rate)
    return t, np.where(t<0, 0, amplitude)

def modified_sine_wave(frequency, duration, sample_rate, amplitude, Offset):
    t = np.linspace(0, duration, sample_rate)
    y = amplitude * np.sin(frequency*2*np.pi*t+Offset * np.pi)
    return t, y
    
def modified_u(start, finish, delay, amplitude, sample_rate):
    t = np.linspace(start, finish, sample_rate)
    return t, np.where(t<0 - delay, 0, amplitude)
    