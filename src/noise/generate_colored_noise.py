import numpy as np
import soundfile as sf

def noise_psd(N, psd = lambda f: 1):
    freqs = np.fft.rfftfreq(N,d=1/44100)
    X_white = np.fft.rfft(np.random.randn(N))
    S = psd(freqs)
    # Normalize S
    S = S / np.sqrt(np.mean(S**2))
    X_shaped = X_white * S 
    return np.fft.irfft(X_shaped)

def PSDGenerator(f):
    return lambda N, sr=44100:noise_psd(N, sr=sr, psd=f)

@PSDGenerator
def white_noise(f):
    return  1

@PSDGenerator
def blue_noise(f):
    return np.sqrt(f)

@PSDGenerator
def violet_noise(f):
    return f

@PSDGenerator
def brownian_noise(f):
    return 1/np.where(f == 0, float('inf'), f)

@PSDGenerator
def pink_noise(f):
    return 1/np.where(f == 0, float('inf'), np.sqrt(f))


def generate_audio_noise(noise_type, duration=5, sr=44100, noise_level=1, output_path=None):
    N = int(sr*duration)
    if noise_type=='white':
        noise = white_noise(len(audio))

    elif noise_type=='pink':
        noise = pink_noise(len(audio))

    elif noise_type=='brown':
        noise = brownian_noise(len(audio))

    elif noise_type=='blue':
        noise = blue_noise(len(audio))

    elif noise_type=='violet':
        noise = violet_noise(len(audio))

    else:
        raise ValueError("Unsupported noise type")

    if output_path is not None:
        sf.write(output_path, noise, sr)

    return noise
    
    
