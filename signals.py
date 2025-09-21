# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 13:05:53 2025

@author: ravra
"""
import numpy as np
def generate_sine_wave(frequency, duration, sample_rate = 44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = np.sin(2 * np.pi * frequency * t)
    return t, y