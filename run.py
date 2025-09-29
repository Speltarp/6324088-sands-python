# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 13:16:48 2025

@author: ravra
"""
import signals as sig
import matplotlib.pyplot as plt

print(sig.generate_sine_wave(5, 2, 100)[0:10])

plt.figure(1)
plt.plot(sig.generate_sine_wave(5, 2, 100))

plt.figure(2)
plt.plot(t, sig.u(-10, 10, -1, 2))
plt.grid(True)
plt.show()


