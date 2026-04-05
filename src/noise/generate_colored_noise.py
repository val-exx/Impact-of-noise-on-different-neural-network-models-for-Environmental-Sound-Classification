import numpy as np
import matplotlib.pyplot as plt
import librosa
import os
import soundfile as sf
import LEVEL


def plot_colored_time(noise,noise_type):
    time = np.arange(start=0,stop=5,step=1/44100)
    if noise_type=='white':
        color='black'
    elif noise_type=='pink':
        color='hotpink'
    else:
        color=noise_type
    plt.plot(time,noise,color)
    plt.title(noise_type.capitalize()+" Noise")
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()
    
def plot_spectrum(s):
    f = np.fft.rfftfreq(len(s),d=1/44100)
    fmin = 50
    fmax = 14000
    idx = np.where((f>=fmin) & (f<=fmax))[0]
    power = np.sum(np.abs(np.fft.rfft(s))[idx])
    print(power)
    return plt.plot(f, 20 * np.log10(np.abs(np.fft.rfft(s))))[0]

def noise_psd(N, psd = lambda f: 1):
    freqs = np.fft.rfftfreq(N,d=1/44100)
    X_white = np.fft.rfft(np.random.randn(N))
    S = psd(freqs)
    # Normalize S
    S = S / np.sqrt(np.mean(S**2))
    X_shaped = X_white * S 
    return np.fft.irfft(X_shaped)

def PSDGenerator(f):
    return lambda N:noise_psd(N,f)

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


def generate_audio_noise(noise_type):
    audio, sr = librosa.load('C:/Users/39347/Desktop/Tesi/from_50_to_20/esc20/audio/1-137-A-32.wav', sr=None)
    if noise_type=='white':
        LEVEL.noise_level = 1
        noise = white_noise(len(audio))
        sf.write('white_noise_{}.wav'.format(LEVEL.noise_level), noise, sr)

    elif noise_type=='pink':
        LEVEL.noise_level = 1
        noise = pink_noise(len(audio))
        sf.write('pink_noise_{}.wav'.format(LEVEL.noise_level), noise, sr)

    elif noise_type=='brown':
        LEVEL.noise_level = 1
        noise = brownian_noise(len(audio))
        sf.write('brown_noise_{}.wav'.format(LEVEL.noise_level), noise, sr)

    elif noise_type=='blue':
        LEVEL.noise_level = 1
        noise = blue_noise(len(audio))
        sf.write('blue_noise_{}.wav'.format(LEVEL.noise_level), noise, sr)

    elif noise_type=='violet':
        LEVEL.noise_level = 1
        noise = violet_noise(len(audio))
        sf.write('violet_noise_{}.wav'.format(LEVEL.noise_level), noise, sr)

def plot_all_colored():
    plt.figure(figsize=(12, 8), tight_layout=True)
    noises = []
    for G, c,noise_type in zip(
        [brownian_noise, pink_noise, white_noise, blue_noise, violet_noise], 
        ['brown','hotpink', 'black', 'blue', 'violet'],
        ['brown','pink','white','blue','violet']):
            if noise_type == 'brown':
                LEVEL.noise_level=1
            else:
                LEVEL.noise_level=1
            noise = G(44100*5)
            noises.append(noise)
            plot_spectrum(noise).set(color=c, linewidth=1)
            plt.xscale('log')
    plt.legend(['brownian', 'pink', 'white', 'blue', 'violet'])
    plt.suptitle("PSD Colored Noise")
    plt.ylabel('Power Spectral Density [dB/Hz]')
    plt.xlabel('Frequency [Hz]')
    plt.grid(True, which="both", ls="-")
    plt.show()

def plot_colored_spec(noise_type):
    
    if noise_type=='white':
        LEVEL.noise_level=1
        noise = white_noise(44100*5)
        color = 'black'
    elif noise_type=='pink':
        LEVEL.noise_level=1 
        noise = pink_noise(44100*5)
        color = 'hotpink'
    elif noise_type=='brown':
        LEVEL.noise_level=1
        noise = brownian_noise(44100*5)
        color = 'brown'
    elif noise_type=='blue':
        LEVEL.noise_level=1 
        noise = blue_noise(44100*5)
        color = 'blue'
    elif noise_type=='violet':
        LEVEL.noise_level=1 
        noise = violet_noise(44100*5)
        color = 'violet'

    plot_colored_time(noise,noise_type)

    plt.figure(figsize=(12, 8))
    plot_spectrum(noise).set(color=color, linewidth=1)
    plt.xscale('log')
    plt.suptitle("PSD {} Noise".format(noise_type.capitalize()))
    plt.ylabel('Power Spectral Density [dB/Hz]')
    plt.xlabel('Frequency [Hz]')
    plt.grid(True, which="both", ls="-")
    plt.show()

plot_all_colored()

