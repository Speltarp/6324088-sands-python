# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 13:16:48 2025

@author: ravra
"""
from signals import generate_sine_wave
import matplotlib.pyplot as plt

print(generate_sine_wave(5, 2, 100)[0:10])

plt.plot(generate_sine_wave(5, 2, 100))
plt.show()

