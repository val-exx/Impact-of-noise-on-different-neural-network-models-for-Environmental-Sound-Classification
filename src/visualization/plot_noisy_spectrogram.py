import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def plot_spectrogram_comparison(audio, noisy_audio, sr, n_fft, hop_length):
    audio_stft = librosa.stft(audio, hop_length=hop_length, n_fft=n_fft)
    noisy_stft = librosa.stft(noisy_audio, hop_length=hop_length, n_fft=n_fft)

    spectrogram = np.abs(audio_stft)
    spectrogram_n = np.abs(noisy_stft)

    log_spectro = librosa.amplitude_to_db(spectrogram)
    log_spectro_n = librosa.amplitude_to_db(spectrogram_n)

    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    librosa.display.specshow(log_spectro, sr=sr, x_axis='time', y_axis='hz', hop_length=hop_length)
    plt.colorbar(label='dB')
    plt.title('Clean audio spectrogram')

    plt.subplot(2, 1, 2)
    librosa.display.specshow(log_spectro_n, sr=sr, x_axis='time', y_axis='hz', hop_length=hop_length)
    plt.colorbar(label='dB')
    plt.title('Noisy audio spectrogram')

    plt.tight_layout()
    plt.show()
