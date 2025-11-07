import numpy as np
import signals as sig

#testing modified_sine_wave(frequency, duration, sample_rate, amplitude, Offset)
def test_modified_sine_wave():
    t, y = sig.modified_sine_wave(2, 1, 1000, 3, 0)
    assert len(t) == 1000
    assert y[0] == 0
    assert np.isclose(max(y), 3, atol=1e-6)

    t, y = sig.modified_sine_wave(1,2, 1000, 2 , 0.5)
    assert len(t) == 2000
    assert y[0] == 2
    assert np.isclose(max(y), 2, atol=1e-6)

#testing pulse(start, stop, amplitude, shift, length, sample_rate=1000)
def test_pulse():
    t, y = sig.pulse(-10, 10, 3, 0, 4)
    assert np.isclose(max(y), 3, atol=1e-6)
    assert y[10000] == 3
    assert len(t) == 20000
    


#testing modified_u(start, finish, delay, amplitude, sample_rate)
def test_modified_u():
    t, y = sig.modified_u(-5, 5, -2, 4, 1000)
    assert np.isclose(max(y), 4, atol=1e-6)
    assert len(t) == 10000
    assert y[5000] == 0
    assert y[9000] == 4