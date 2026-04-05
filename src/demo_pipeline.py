import numpy as np
import librosa

from src.noise.generate_colored_noise import generate_audio_noise
from src.noise.signal_power import model_frequency_band
from src.visualization.plot_noisy_spectrogram import plot_spectrogram_comparison
from src.evaluation.compute_confusion_matrix import compute_confusion_matrix


class DummyModel:
    """
    Placeholder model used only to show the evaluation flow.
    Replace this with a real model wrapper.
    """
    def predict(self, audio):
        return 0


def mix_audio_and_noise(audio, noise, snr_db):
    """
    Simple placeholder mixing function.
    If you already have a more precise SNR-based function, use that instead.
    """
    if len(noise) < len(audio):
        repeats = int(np.ceil(len(audio) / len(noise)))
        noise = np.tile(noise, repeats)

    noise = noise[:len(audio)]

    audio_power = np.mean(audio ** 2)
    noise_power = np.mean(noise ** 2)

    if noise_power == 0:
        return audio

    alpha = np.sqrt((audio_power * 10 ** (-snr_db / 10)) / noise_power)
    noisy_audio = audio + alpha * noise
    return noisy_audio


def run_demo_pipeline(audio_path, model_name='htsat', noise_type='pink', snr_db=5):
    """
    Demo pipeline:
    1. load audio
    2. generate colored noise
    3. mix clean audio and noise
    4. plot clean vs noisy spectrogram
    5. run dummy inference
    6. build a dummy confusion matrix example
    """
    if model_name == 'mn40as':
        sr = 32000
        n_fft = 800
        hop_length = 320
    elif model_name == 'htsat':
        sr = 32000
        n_fft = 1024
        hop_length = 320
    elif model_name == 'tfnet':
        sr = 44100
        n_fft = 1764
        hop_length = 882
    else:
        raise ValueError('Model not supported')

    audio, sr = librosa.load(audio_path, sr=sr)

    noise = generate_audio_noise(
        noise_type=noise_type,
        duration=len(audio) / sr,
        sr=sr,
        noise_level=1
    )

    noisy_audio = mix_audio_and_noise(audio, noise, snr_db)

    plot_spectrogram_comparison(
        audio=audio,
        noisy_audio=noisy_audio,
        sr=sr,
        n_fft=n_fft,
        hop_length=hop_length
    )

    model = DummyModel()
    pred = model.predict(noisy_audio)

    y_true = [0]
    y_pred = [pred]
    cm = compute_confusion_matrix(y_true, y_pred, num_classes=19)

    print("Demo pipeline executed successfully.")
    print("Model:", model_name)
    print("Noise type:", noise_type)
    print("SNR [dB]:", snr_db)
    print("Prediction:", pred)
    print("Confusion matrix:")
    print(cm)


if __name__ == '__main__':
    run_demo_pipeline(
        audio_path='example.wav',
        model_name='htsat',
        noise_type='pink',
        snr_db=5
    )
