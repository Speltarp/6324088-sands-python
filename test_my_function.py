import numpy as np
import signals as sig

#testing modified_sine_wave(frequency, duration, sample_rate, amplitude, Offset)
def test_modified_sine_wave():
    '''
    Tests the modified_sine_wave functions with various tests.
    
    The tests check:
        - If the signal has the correct length
        - If the initial value is correct
        - If the amplitude is correct

    '''
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
    '''
    Tests the pulse function with various tests
    
    The tests check:
        - If the amplitude is correct
        - If the pulse happens at the correct time
        - If the length is correct

    '''
    t, y = sig.pulse(-10, 10, 3, 0, 4)
    assert np.isclose(max(y), 3, atol=1e-6)
    assert y[10000] == 3
    assert len(t) == 20000
    

#testing modified_u(start, finish, delay, amplitude, sample_rate)
def test_modified_u():
    '''
    Tests the modified unit step function with various tests
    
    The tests check:
        - If the amplitude is correct
        - If the length is correct
        - If the functions steps at the correct time

    '''
    t, y = sig.modified_u(-5, 5, -2, 4, 1000)
    assert np.isclose(max(y), 4, atol=1e-6)
    assert len(t) == 10000
    assert y[5000] == 0
    assert y[9000] == 4
    
#testing generate_sine_wave(frequency, duration, sample_rate)
def test_generate_sine_wave():
    '''
    Tests the generate_sine_wave function with various tests
    
    The tests check:
        - If the length of the function is correct
        - If the initial value is correct
        - If the amplitude is correct

    '''
    t,y = sig.generate_sine_wave(2, 2, 10000)
    assert len(t) == 20000
    assert y[0] == 0
    assert np.isclose(max(y), 1, atol=1e-6)

#testing u(start, finish, amplitude, sample_rate)
def test_u():
    '''
    Tests the unit step function with various tests
    
    The tests check:
        - If the length of the function is correct
        - If the function steps at the correct time

    '''
    t, y = sig.u(-4, 4, 4, 1000)
    len(t) == 8000
    assert y[3000] == 0
    assert y[5000] == 4
    


    