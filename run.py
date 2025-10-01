# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 13:16:48 2025

@author: ravra
"""
import signals as sig
import matplotlib.pyplot as plt

#generate a sine wave
print(sig.generate_sine_wave(5, 2, 100)[0:10])

t, y = sig.generate_sine_wave(5, 2, 100)
plt.figure(1)
plt.plot(t, y)
plt.grid(True)
plt.title("Sine wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")

#generate unit step function
t, y = sig.u(-10, 10, -2, 3, 1000)
plt.figure(2)
plt.plot(t, y)
plt.grid(True)
plt.title("Unit Step function")
plt.xlabel("Time")
plt.ylabel("Height")
plt.show()

t, y = sig.modified_sine_wave(5, 2, 1000, 3, 0.5)
plt.figure(3)
plt.plot(t, y)
plt.show()
