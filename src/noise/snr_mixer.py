import numpy as np
from src.noise.signal_power import bandpower

def adjust_noise_length(noise_audio, target_length):
    if len(noise_audio) < target_length:
        repeats = int(np.ceil(target_length / len(noise_audio)))
        noise_audio = np.tile(noise_audio, repeats)

    noise_audio = noise_audio[:target_length]
    return noise_audio

def mix_audio_at_snr(noise_audio, target_audio, sr, fmin, fmax, SNR):
    noise_audio = adjust_noise_length(noise_audio, len(target_audio))

    P_x = bandpower(target_audio, sr, fmin, fmax)
    P_n0 = bandpower(noise_audio, sr, fmin, fmax)

    if P_n0 == 0:
        raise ValueError("Noise power is zero, cannot scale noise.")

    alpha = np.sqrt((P_x * 10 ** (-SNR / 10)) / P_n0)

    noisy_audio = target_audio + noise_audio * alpha

    return noisy_audio

def mix_audio_for_model(noise_audio, target_audio, sr, model, SNR):
    if model == 'mn40as' :
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

    noisy_audio = mix_audio_at_snr(noise_audio, target_audio, sr, fmin, fmax, SNR)
    return noisy_audio
