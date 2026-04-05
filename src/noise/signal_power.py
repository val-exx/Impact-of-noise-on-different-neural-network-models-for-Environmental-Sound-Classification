import scipy
import numpy as np

def compute_power(input_signal):
    samples = np.abs(input_signal) ** 2
    sum_samples = 0.0
    for sample in samples:
        sum_samples = sum_samples + sample
    N = len(input_signal)
    power_signal = sum_samples / N
    return power_signal

def bandpower(x, fs, fmin, fmax):
    f, Pxx = scipy.signal.periodogram(x, fs=fs)
    ind_min = scipy.argmax(f > fmin) - 1
    ind_max = scipy.argmax(f > fmax) - 1
    return scipy.trapz(Pxx[ind_min:ind_max], f[ind_min:ind_max])

def model_frequency_band(model):
    fmin = 0
    fmax = 0

    if model == 'mn40as' or model == 'mn40_as':
        fmin = 0
        fmax = 15000
    elif model == 'htsat':
        fmin = 50
        fmax = 14000
    elif model == 'tfnet':
        fmin = 50
        fmax = 11025
    else:
        raise ValueError('Model not supported')

    return fmin, fmax
