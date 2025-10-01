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

def u(start, finish, delay, amplitude, sample_rate):
    t = np.linspace(start, finish, sample_rate)
    return t, np.where(t<0 - delay, 0, amplitude)
#
#def modifier(type_function, start, finish, delay, amplitude, sample_rate, frequency, duration, offset, extra_delay, extra_amplitude, extra_frequency):
 #   if type_function == "u":
  #      t, y = u(start, finish, delay + extra_delay, amplitude + extra_amplitude, sample_rate)
   #     
    #if type_function == "sin":
     #   t, y = generate_sine_wave(frequency + extra_frequency, duration, amplitude + extra_amplitude)
    #return t, y


#import matplotlib.pyplot as plt

#t1, y1 = modifier("u", -10, 10, -2, 3, 1000, 0, 0, 0, -2, 2, 0)
#plt.figure()
#plt.show(t1, y1)

def modified_sine_wave(frequency, duration, sample_rate, amplitude, Offset):
    t = np.linspace(0, duration, sample_rate)
    y = amplitude * np.sin(frequency*2*np.pi*t+Offset * np.pi)
    return t, y
    
    