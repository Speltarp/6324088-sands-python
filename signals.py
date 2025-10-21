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
    sample_rate : Integer.
    Amount of plotted points per second.

    Returns
    -------
    y : numpy.ndarray
    Amplitude
    t : numpy.ndarray
    Time

    """
    t = np.linspace(0, duration, sample_rate)
    y = np.sin(frequency*2*np.pi*t)
    return t, y

def u(start, finish, amplitude, sample_rate):
    """
    generates a unit step function

    Parameters
    ----------
    start : Float.
    Moment in time where the function starts
    finish : Float.
    Moment in time where function ends
    amplitude : Float
    Height of the unit step function
    sample_rate : Integer.
    Amount of plotted points per second

    Returns
    -------
    t : numpy.ndarray
    Time
    y : numpy.ndarray
    The amplitude values (0 for t<0, 'amplitude' for t>0)

    """
    t = np.linspace(start, finish, sample_rate)
    y = np.where(t<0, 0, amplitude)
    return t, y 

def pulse(start, stop, amplitude, shift, length, sample_rate=1000):
    '''
    Creates a pulse

    Parameters
    ----------
    start : Float.
    Moment in time where function starts
    stop : Float.
    Moment in time where function stops
    amplitude : Float.
    Height of the pulse
    shift : Float.
    Moves the pulse function in time
    length : Float.
    How long the pulse lasts for
    sample_rate : Integer.
    Amount of plotted points per second.

    Returns
    -------
    t : numpy.ndarray
    Time
    y : numpy.ndarray
    The amplitude

    '''
    t = np.linspace(start, stop, sample_rate)
    y = np.where((1/length)*np.abs(t-shift) <= 0.5, amplitude, 0)
    return t, y

def modified_sine_wave(frequency, duration, sample_rate, amplitude, Offset):
    """
    generates a modified sine wave

    Parameters
    ----------
    frequency : Float.
    Number of cycli the wave does per second, measured in Hertz
    duration : Float.
    How long the sine wave continues for.
    sample_rate : Integer.
    Amount of plotted points per second.
    amplitude : Float.
    Highest point of the sine wave
    Offset : Float
    Horizontal shift of the sine wave along the time axis

    Returns
    -------
    y : numpy.ndarray
    Amplitude
    t : numpy.ndarray
    Time

    """
    t = np.linspace(0, duration, sample_rate)
    y = amplitude * np.sin(frequency*2*np.pi*t+Offset * np.pi)
    return t, y
    
def modified_u(start, finish, delay, amplitude, sample_rate):
    """
    generates a modified unit step function

    Parameters
    ----------
    start : Float.
    Moment in time where the function starts
    finish : Float.
    Moment in time where function ends
    delay : Float
    Delays the unit step function (seconds)
    amplitude : Float
    Height of the unit step function
    sample_rate : Integer.
    Amount of plotted points per second

    Returns
    -------
    t : numpy.ndarray
    Time
    y : numpy.ndarray
    The amplitude values (0 for t<0, 'amplitude' for t>0)

    """
    t = np.linspace(start, finish, sample_rate)
    y = np.where(t<0 - delay, 0, amplitude)
    return t, y
    