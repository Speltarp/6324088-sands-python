#refactor means restructuring your code
#write test first
import numpy as np
def generate_sine_wave(frequency, amplitude, duration, sample_rate=1000):
    t = np.linspace(0, duration, int(duration*sample_rate))
    y = amplitude*np.sin(frequency*2*np.pi*t)
    return t, y

t, y = generate_sine_wave(1,2,1)
assert len(t) == 1000
assert y[0] == 0
assert np.isclose(max(y), 2, atol=1e-6)

def u(start, finish, amplitude, sample_rate=1000):
    t = np.linspace(start, finish, sample_rate)
    y = np.where(t<0, 0, amplitude)
    return t, y 

t,y = u(-10, 10, 3)
assert y[0] == 0