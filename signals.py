# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 13:05:53 2025

@author: ravra
"""
import numpy as np
def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, sample_rate)
    y = np.sin(frequency*2*np.pi*t)
    return y
