import numpy as np
import signals as sig

def test_modified_sine_wave():
    t, y = sig.modified_sine_wave(2, 1, 1000, 3, 0)
    assert len(t) == 1000
    assert y[0] == 0
    assert np.isclose(max(y), 3, atol=1e-6)

t, y = sig.modified_sine_wave(1,2, 1000, 2 , 0.5)
assert len(t) == 1000
assert y[0] == 2
assert np.isclose(max(y), 2, atol=1e-6)